from setuptools import setup

setup(
    name='cathy',
    version='0.1.5',
    description='Discord chat bot using AIML artificial intelligence.',
    url='https://github.com/NanoDano/ChattyCathy',
    author='DevDungeon',
    author_email='nanodano@devdungeon.com',
    license='GPL-3.0',
    packages=['cathy'],  # The folder with the real code
    scripts=['bin/cathy'],  # List of executable scripts to include
    zip_safe=False,
    install_requires=[
        'docopt',
        # '',
    ]
)
