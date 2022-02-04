import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1185"
version_tuple = (0, 0, 1185)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1185")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1061"
data_version_tuple = (0, 0, 1061)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1061")
except ImportError:
    pass
data_git_hash = "cef3660e74f606f49d18df2fc0e27a858bbd4579"
data_git_describe = "v0.0-1061-gcef3660"
data_git_msg = """\
commit cef3660e74f606f49d18df2fc0e27a858bbd4579
Merge: 6ff3b24 2491aa7
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Fri Feb 4 11:43:42 2022 +1100

    Merge pull request #345 from antonblanchard/popcnt-go-fast
    
    popcnt* timing improvements from Paul

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
