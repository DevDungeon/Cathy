from setuptools import setup

setup(
    name='cathy',
    version='3.1.3',
    description='Discord chat bot using AIML artificial intelligence.',
    long_description="See https://github.com/DevDungeon/cathy",
    url='https://github.com/DevDungeon/ChattyCathy',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    packages=['cathy'],
    entry_points={
        'console_scripts': [
            'cathy = cathy.__main__:main',
        ],
    },
    package_data={
        'cathy': [
            'std-startup.xml',
            'aiml/alice/*.aiml',
            'aiml/custom/*.aiml'
        ],
    },
    zip_safe=False,
    install_requires=[
        'aiohttp==3.6.2',
        'async-timeout==3.0.1',
        'attrs==19.3.0',
        'certifi==2019.11.28',
        'chardet==3.0.4',
        'discord.py==1.3.1',
        'docopt==0.6.2',
        'idna==2.9',
        'multidict==4.7.5',
        'python-aiml==0.9.3',
        'requests==2.23.0',
        'urllib3==1.25.8',
        'websockets==8.1',
        'yarl==1.4.2',
    ],
    python_requires='>=3.7',
)
