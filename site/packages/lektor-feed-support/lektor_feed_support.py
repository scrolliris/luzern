import hashlib
import uuid
from datetime import datetime, date

import pkg_resources
from lektor.build_programs import BuildProgram
from lektor.db import F
from lektor.environment import Expression
from lektor.pluginsystem import Plugin
from lektor.context import get_ctx, url_to
from lektor.reporter import reporter
from lektor.sourceobj import VirtualSourceObject
from lektor.utils import build_url

from werkzeug.contrib.atom import AtomFeed
from markupsafe import escape


def get_id(s):
    b = hashlib.md5(s.encode('utf-8')).digest()
    return uuid.UUID(bytes=b, version=3).urn


def get_value(item, field, default=None):
    if field in item:
        return str(item[field])
    return default


def get_items(ctx, feed_source):
    if feed_source.items:
        expr = Expression(ctx.env, feed_source.items)
        items = expr.evaluate(ctx.pad)
    else:
        items = feed_source.parent.children

    if feed_source.item_model:
        items = items.filter(F._model == feed_source.item_model)

    order_by = '-' + feed_source.item_date_field
    return items.order_by(order_by).limit(int(feed_source.limit))


def make_feed(feed_source, project_id):
    post = feed_source.parent

    summary = get_value(post, feed_source.summary_field) or ''
    if hasattr(summary, '__html__'):
        subtitle_type = 'html'
        summary = (summary.__html__())
    else:
        subtitle_type = 'text'
    author = get_value(post, feed_source.author_field) or ''
    generator = ('Lektor Feed Support Plugin',
                 '',
                 pkg_resources.get_distribution('lektor-feed-support').version)

    return AtomFeed(
        title=feed_source.feed_name,
        subtitle=summary,
        subtitle_type=subtitle_type,
        author=author,
        feed_url=url_to(feed_source, external=True),
        url=url_to(post, external=True),
        id=get_id(project_id),
        generator=generator,
    )


class FeedSource(VirtualSourceObject):
    def __init__(self, parent, prefix, plugin):
        VirtualSourceObject.__init__(self, parent)
        self.plugin = plugin
        self.prefix = prefix

    @property
    def path(self):
        return self.parent.path + '@feed/' + self.prefix

    @property
    def url_path(self):
        _path = self.plugin.get_feed_support_config(self.prefix, 'url_path')
        if _path:
            return _path

        return build_url([self.parent.url_path, self.filename])

    def __getattr__(self, item):
        try:
            return self.plugin.get_feed_support_config(self.prefix, item)
        except KeyError:
            raise AttributeError(item)

    @property
    def feed_name(self):
        return self.plugin.get_feed_support_config(
             self.prefix, 'name') or self.prefix


class FeedItem(object):
    def __init__(self, item, source):
        self.item = item
        self.source = source

    @property
    def author(self):
        return get_value(self.item, self.source.item_author_field)

    @property
    def url(self):
        return url_to(self.item, external=True)

    @property
    def title(self):
        field = self.source.item_title_field
        if field in self.item:
            return self.item[field]
        return self.item.record_label

    @property
    def body(self):
        field = self.source.item_body_field
        if field not in self.item:
            raise RuntimeError(
                'Body field %r not found in %r' % (field, self.item))
        return str(escape(self.item[field]))

    @property
    def updated(self):
        field = self.source.item_date_field
        if field in self.item:
            updated = self.item[field]
        else:
            updated = datetime.utcnow()
        if isinstance(updated, date) and not isinstance(updated, datetime):
            updated = datetime(*updated.timetuple()[:3])
        return updated


class FeedBuildProgram(BuildProgram):
    def produce_artifacts(self):
        self.declare_artifact(
            self.source.url_path,
            sources=list(self.source.iter_source_filenames()))

    def build_artifact(self, artifact):
        ctx = get_ctx()
        feed_source = self.source
        project_id = ctx.env.project.id

        feed = make_feed(self.source, project_id)
        for item in get_items(ctx, feed_source):
            try:
                _id = get_id('{0}/{1}'.format(
                    project_id, item['_path'].encode('utf-8'))),

                with ctx.changed_base_url(item.url_path):
                    feed_item = FeedItem(item, feed_source)

                feed.add(
                    feed_item.title,
                    feed_item.body,
                    xml_base=feed_item.url,
                    url=feed_item.url,
                    content_type='html',
                    id=_id,
                    author=feed_item.author,
                    updated=feed_item.updated,
                )
            except Exception as exc:
                reporter.report_generic(exc)

        with artifact.open('wb') as f:
            f.write(feed.to_string().encode('utf-8'))


class FeedSupportPlugin(Plugin):
    name = 'Feed Support'
    description = 'Adds feed support to Lektor.'

    defaults = {
        'source_path': '/',
        'name': None,
        'url_path': None,
        'filename': 'feed.xml',
        'limit': 30,
        'author_field': 'author',
        'summary_field': 'summary',
        'items': None,
        'item_title_field': 'title',
        'item_body_field': 'body',
        'item_author_field': 'author',
        'item_date_field': 'pub_date',
        'item_model': None,
    }

    def get_feed_support_config(self, prefix, key):
        return self.get_config().get(
            '{0}.{1}'.format(prefix, key), self.defaults[key])

    def on_setup_env(self, **extra):
        self.env.add_build_program(FeedSource, FeedBuildProgram)

        @self.env.virtualpathresolver('feed')
        def resolve_virtual_path(record, pieces):
            if not pieces:
                return

            key = pieces[0]

            config = self.get_config()
            if key not in config.sections():
                return

            source_path = self.get_feed_support_config(key, 'source_path')
            if record.path == source_path:
                return FeedSource(record, key, plugin=self)

        @self.env.generator
        def generate_feeds(node):
            # reads [section] from configs/feed-support.ini
            for prefix in self.get_config().sections():
                if node.path == self.get_feed_support_config(
                    prefix, 'source_path'):
                    yield FeedSource(node, prefix, self)
