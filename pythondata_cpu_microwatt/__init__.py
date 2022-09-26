import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1390"
version_tuple = (0, 0, 1390)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1390")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1248"
data_version_tuple = (0, 0, 1248)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1248")
except ImportError:
    pass
data_git_hash = "d9c55defdb3175e84a3fe1722cf6abca977484c0"
data_git_describe = "v0.0-1248-gd9c55de"
data_git_msg = """\
commit d9c55defdb3175e84a3fe1722cf6abca977484c0
Merge: d3fb263 ed58073
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Sep 26 16:47:15 2022 +1000

    Merge pull request #407 from shingarov/openocd-012
    
    Recognize version string "0.12" in recent OpenOCD master

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
