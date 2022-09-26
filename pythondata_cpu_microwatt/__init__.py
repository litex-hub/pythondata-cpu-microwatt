import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1392"
version_tuple = (0, 0, 1392)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1392")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1250"
data_version_tuple = (0, 0, 1250)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1250")
except ImportError:
    pass
data_git_hash = "5766dbab372f705184dd869c7448633be1b81c7b"
data_git_describe = "v0.0-1250-g5766dba"
data_git_msg = """\
commit 5766dbab372f705184dd869c7448633be1b81c7b
Merge: d9c55de 6c3f7d7
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Sep 26 16:49:11 2022 +1000

    Merge pull request #406 from shingarov/spi-kintex
    
    Add support for flashing the s25fl256s onboard Genesys2

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
