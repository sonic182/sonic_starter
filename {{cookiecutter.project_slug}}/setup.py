"""Setup module."""

from setuptools import setup
from setuptools import find_packages
from pkg_resources import parse_requirements


def read_file(filename):
    """Read file correctly."""
    with open(filename) as _file:
        return _file.read().strip()


def requirements(filename):
    """Parse requirements from file."""
    return [str(req) for req in parse_requirements(read_file(filename))]


setup(
    name='{{cookiecutter.project_slug}}',
    version='0.0.1',
    description='{{cookiecutter.project_description}}',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    license='MIT',
    packages=find_packages(),
    setup_requires=['pytest-runner'],
    install_requires=requirements('./requirements.txt'),
    extras_require={
        'test': requirements('./test-requirements.txt')
    }
)
