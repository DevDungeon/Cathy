from setuptools import setup


def readme_file_contents():
    with open('README.md') as f:
        data = f.read()
    return data


setup(
    name='cathy',
    version='1.1.2',
    description='Discord chat bot using AIML artificial intelligence.',
    long_description=readme_file_contents(),
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
        'docopt',
        'python-aiml',
        'discord.py',
        'requests'
    ]
)
