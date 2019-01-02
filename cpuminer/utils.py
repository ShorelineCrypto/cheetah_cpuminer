
################################################################################
# Preamble.
################################################################################

# Python standard library imports.
import collections
import inspect
import itertools
import logging
import math
import platform
import os
import os.path
import subprocess
import sys
import tempfile
import time


#from exceptions import CustomParamException

log_name = os.path.join(tempfile.gettempdir(),  os.path.basename(__file__) + '.log')
logging.basicConfig(filename=log_name)
l = logging.getLogger(__name__)  # module logger


################################################################################
# Helper functions.
################################################################################

def getPathOfThisFile():
    """Get absolute path of the file from which this function is called.

    This seems to be the most portable solution:
    https://stackoverflow.com/a/6628348
    """

    l.debug('Starting function...')

    return os.path.abspath(os.path.realpath(inspect.stack()[1][1]))


def properClose(fileObj):
    """Close the file object in a super-paranoid way, i.e. ensuring that all buffered output is flushed to it by the OS.

    This is very useful for situations where you write to a file on disk, and then downstream code needs to open that file from disk for reading.
    The downstream code may open a partially-written file, which would be bad.
    Calling this function would ensure the file is safely written out to completion prior to moving on.
    """

    l.debug('Starting function...')

    fileObj.flush()
    os.fsync(fileObj.fileno())
    fileObj.close()


def isReadable(filePath):
    """Test if the file at this path is readable, returning boolean test result; if not readable, log reason why as error.
    """
    try:
        f = open(filePath, 'r')
        f.close()
    except IOError, e:
        l.error('Cannot open for reading: {}'.format(filePath))
        l.error('Reason: {}'.format(e))
        return False
    return True


def isWriteable(filePath):
    """Test if the file at this path is writeable, returning boolean test result; if not writeable, log reason why as error.

    Note this test file by actually writing to it, then removing it.
    So if the file already exists, it will clobbered, then deleted!
    """
    try:
        f = open(filePath, 'w')
        properClose(f)
        os.remove(f.name)
    except IOError, e:
        l.error('Cannot open for writing: {}'.format(filePath))
        l.error('Reason: {}'.format(e))
        return False
    return True

