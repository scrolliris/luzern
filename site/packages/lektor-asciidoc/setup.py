from setuptools import setup

setup(
    name='lektor-asciidoc',
    version='0.1',
    py_modules=['lektor_asciidoc'],
    entry_points={
        'lektor.plugins': [
            'asciidoc = lektor_asciidoc:AsciiDocPlugin',
        ]
    },
    install_requires=[]
)
