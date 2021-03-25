import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post999"
version_tuple = (0, 0, 999)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post999")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post904"
data_version_tuple = (0, 0, 904)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post904")
except ImportError:
    pass
data_git_hash = "6d827b93580684e5977f5d7340ed128521161f42"
data_git_describe = "v0.0-904-g6d827b9"
data_git_msg = """\
commit 6d827b93580684e5977f5d7340ed128521161f42
Merge: 0af9062 be11ebb
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu Mar 25 14:43:45 2021 +1100

    Merge pull request #286 from antonblanchard/Makefile-cleanup-3
    
    A few more Makefile cleanups

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
