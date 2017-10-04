from setuptools import setup

setup(
    name='lektor-feed-support',
    version='0.1',
    py_modules=['lektor_feed_support'],
    install_requires=[
        'MarkupSafe'
    ],
    entry_points={
        'lektor.plugins': [
            'feed-support = lektor_feed_support:FeedSupportPlugin',
        ]
    },
)
