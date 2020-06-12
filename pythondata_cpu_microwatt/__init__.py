import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post676"
version_tuple = (0, 0, 676)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post676")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post616"
data_version_tuple = (0, 0, 616)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post616")
except ImportError:
    pass
data_git_hash = "7577cb18fbd92ee3f5acad9084e4fe700092255a"
data_git_describe = "v0.0-616-g7577cb1"
data_git_msg = """\
commit 7577cb18fbd92ee3f5acad9084e4fe700092255a
Merge: 6bb3837 9653b29
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Fri Jun 12 10:25:09 2020 +1000

    Merge pull request #201 from mikey/github-actions
    
    Move from travis to github workflows

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
