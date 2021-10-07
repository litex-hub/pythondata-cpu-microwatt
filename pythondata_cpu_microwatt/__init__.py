import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1148"
version_tuple = (0, 0, 1148)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1148")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1036"
data_version_tuple = (0, 0, 1036)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1036")
except ImportError:
    pass
data_git_hash = "9cbe1f4a178bdb7f6fd1b35cddfaeace7c249821"
data_git_describe = "v0.0-1036-g9cbe1f4"
data_git_msg = """\
commit 9cbe1f4a178bdb7f6fd1b35cddfaeace7c249821
Merge: 099862b 2d142a6
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Sep 28 09:06:18 2021 +1000

    Merge pull request #334 from antonblanchard/icbi-issue
    
    Add a test for icbi and dcbz issues

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
