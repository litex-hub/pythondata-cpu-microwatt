import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post990"
version_tuple = (0, 0, 990)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post990")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post895"
data_version_tuple = (0, 0, 895)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post895")
except ImportError:
    pass
data_git_hash = "ef01fa32bd888215ffc688389296f17676667590"
data_git_describe = "v0.0-895-gef01fa3"
data_git_msg = """\
commit ef01fa32bd888215ffc688389296f17676667590
Merge: 6523acc 91a53d8
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue Mar 23 20:02:27 2021 +1100

    Merge pull request #284 from antonblanchard/boot-clocks
    
    Allow SPI BOOT_CLOCKS to be overridden by top level

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
