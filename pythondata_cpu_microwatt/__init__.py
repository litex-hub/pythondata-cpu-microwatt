import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post603"
version_tuple = (0, 0, 603)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post603")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post552"
data_version_tuple = (0, 0, 552)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post552")
except ImportError:
    pass
data_git_hash = "354e0fbfea8e0771640522e2c816e8ac13c89229"
data_git_describe = "v0.0-552-g354e0fb"
data_git_msg = """\
commit 354e0fbfea8e0771640522e2c816e8ac13c89229
Merge: 6692f0d 5860c2d
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue May 19 14:27:42 2020 +1000

    Merge pull request #171 from shenki/mw-debug-features
    
    mw debug features

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
