"""Setup module."""

import re
from setuptools import setup

RGX = re.compile('(\w+==[\d.]+)')


def read_file(filename):
    """Read file correctly."""
    with open(filename) as _file:
        return _file.read().strip()


def parse_requirements(filename):
    """Parse requirements from file."""
    return re.findall(RGX, read_file(filename)) or []


setup(
    name='{{cookiecutter.project_slug}}',
    version='0.0.1',
    description='{{cookiecutter.project_description}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    license='MIT',
    packages=['{{cookiecutter.project_slug}}'],
    setup_requires=['pytest-runner'],
    test_requires=['pytest'],
    install_requires=parse_requirements('requirements.txt'),
    extras_require={
        'dev': parse_requirements('dev-requirements.txt'),
        'test': parse_requirements(
            'dev-requirements.txt') + ['coverage', 'coveralls']
    }
)
