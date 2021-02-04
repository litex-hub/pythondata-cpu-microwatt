import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post934"
version_tuple = (0, 0, 934)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post934")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post848"
data_version_tuple = (0, 0, 848)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post848")
except ImportError:
    pass
data_git_hash = "5f8279a14ab2921df91babd684f6a4991c59ac29"
data_git_describe = "v0.0-848-g5f8279a"
data_git_msg = """\
commit 5f8279a14ab2921df91babd684f6a4991c59ac29
Merge: 45b7312 740f013
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Thu Jan 7 14:47:11 2021 +1100

    Merge pull request #263 from antonblanchard/reset-pid
    
    Initialize PID register

"""

# Tool version info
tool_version_str = "0.0.post86"
tool_version_tuple = (0, 0, 86)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post86")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
