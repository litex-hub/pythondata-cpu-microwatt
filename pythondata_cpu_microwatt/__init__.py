import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1187"
version_tuple = (0, 0, 1187)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1187")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1063"
data_version_tuple = (0, 0, 1063)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1063")
except ImportError:
    pass
data_git_hash = "5a5a0826017c9acd45f39bda48c449017997ecb7"
data_git_describe = "v0.0-1063-g5a5a082"
data_git_msg = """\
commit 5a5a0826017c9acd45f39bda48c449017997ecb7
Merge: cef3660 286757f
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Mon Feb 7 17:57:08 2022 +1100

    Merge pull request #343 from mikey/orange-crab-ci
    
    ci: Add new Orange Crab build

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
