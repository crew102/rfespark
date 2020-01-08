from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md')) as f:
    long_description = f.read()

setup(
    name='rfespark',
    version='0.0.0.9000',
    description='Recursive Feature Elimination on Spark',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Christopher Baker, Matthew Bowman, Brady Wilkerson',
    author_email='chriscrewbaker@gmail.com',
    license='LICENSE.txt',
    packages=['rfespark'],
    install_requires=['pyspark'],
    tests_require=['pytest'],
    setup_requires=['pytest-runner']
)
