import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1181"
version_tuple = (0, 0, 1181)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1181")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1059"
data_version_tuple = (0, 0, 1059)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1059")
except ImportError:
    pass
data_git_hash = "6ff3b2499ceaf911252f634d44469fefb58952ae"
data_git_describe = "v0.0-1059-g6ff3b24"
data_git_msg = """\
commit 6ff3b2499ceaf911252f634d44469fefb58952ae
Merge: fda8879 cdd661d
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jan 18 13:27:27 2022 +1100

    Merge pull request #342 from mkj/orangecrab-merge
    
    Orangecrab working with litedram
    
    Fixed up a few simple merge conflicts in the Makefile.

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
