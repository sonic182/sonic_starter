"""Setup module."""

from setuptools import setup


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
    install_requires=[],
    extras_require={
        'test': [
            'pytest',
            'pytest-cov',
            'pytest-sugar',
            'coverage',
            'coveralls'
        ]
    }
)
