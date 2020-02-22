from setuptools import setup

setup(
    name='cathy',
    version='2.1.1',
    description='Discord chat bot using AIML artificial intelligence.',
    long_description=open('README.rst').read(),
    url='https://github.com/DevDungeon/ChattyCathy',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    packages=['cathy'],
    scripts=[
        'bin/cathy',
        'bin/cathy.bat',
    ],
    package_data={
        'cathy': [
            'std-startup.xml',
            'aiml/alice/*.aiml',
            'aiml/custom/*.aiml'
        ],
    },
    zip_safe=False,
    install_requires=[
        'aiohttp==1.0.5',
        'async-timeout==3.0.0',
        'cathy==2.1.1',
        'certifi==2018.4.16',
        'chardet==3.0.4',
        'discord.py==0.16.12',
        'docopt==0.6.2',
        'idna==2.7',
        'multidict==4.3.1',
        #'pkg-resources',
        'python-aiml==0.9.1',
        'requests==2.20.0',
        'urllib3==1.23',
        'websockets==3.4',
    ],
    python_requires='==3.6.8',
)
