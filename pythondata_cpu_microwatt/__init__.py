import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1242"
version_tuple = (0, 0, 1242)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1242")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1100"
data_version_tuple = (0, 0, 1100)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1100")
except ImportError:
    pass
data_git_hash = "d3aff67fa77b5d24aa961c5e43a550f8a4d95a58"
data_git_describe = "v0.0-1100-gd3aff67"
data_git_msg = """\
commit d3aff67fa77b5d24aa961c5e43a550f8a4d95a58
Merge: 1ff852b 71d4b5e
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Mon Jun 13 07:15:55 2022 +1000

    Merge pull request #375 from antonblanchard/core_debug-init
    
    core_debug: Initialise gspr_index

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
