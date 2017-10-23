"""Settings module."""
from os.path import dirname
from os.path import join
from os.path import abspath


def basepath(*args):
    """Get files from basepath."""
    return join(dirname(dirname(dirname(abspath(__file__)))), *args)
