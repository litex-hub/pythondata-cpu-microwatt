import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post985"
version_tuple = (0, 0, 985)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post985")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post893"
data_version_tuple = (0, 0, 893)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post893")
except ImportError:
    pass
data_git_hash = "6523acc74344b95e7cceb83611fb8cb2a030c1a3"
data_git_describe = "v0.0-893-g6523acc"
data_git_msg = """\
commit 6523acc74344b95e7cceb83611fb8cb2a030c1a3
Merge: 6c76890 d26a157
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Feb 9 10:06:03 2021 +1100

    Merge pull request #274 from mikey/read-sprs
    
    Fix reading DSISR/DAR before writing and add a test to read from all SPRs

"""

# Tool version info
tool_version_str = "0.0.post92"
tool_version_tuple = (0, 0, 92)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post92")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
