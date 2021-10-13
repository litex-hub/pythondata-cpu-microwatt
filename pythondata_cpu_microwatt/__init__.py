import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1150"
version_tuple = (0, 0, 1150)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1150")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1038"
data_version_tuple = (0, 0, 1038)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1038")
except ImportError:
    pass
data_git_hash = "8a030502a22c206d2efefe28415ff367bc01c4f6"
data_git_describe = "v0.0-1038-g8a03050"
data_git_msg = """\
commit 8a030502a22c206d2efefe28415ff367bc01c4f6
Merge: 9cbe1f4 a5c9b3c
Author: Michael Neuling <mikey@neuling.org>
Date:   Wed Oct 13 17:44:47 2021 +1100

    Merge pull request #336 from paulusmack/fixes
    
    Makefile: Correct parameters for the Orange Crab 85F

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
