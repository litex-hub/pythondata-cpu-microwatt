import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1169"
version_tuple = (0, 0, 1169)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1169")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1047"
data_version_tuple = (0, 0, 1047)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1047")
except ImportError:
    pass
data_git_hash = "fda8879e2f721e4a01f8f9e946ac9cf6d1d1a363"
data_git_describe = "v0.0-1047-gfda8879"
data_git_msg = """\
commit fda8879e2f721e4a01f8f9e946ac9cf6d1d1a363
Merge: ffbf2f9 5e90133
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jan 18 11:51:54 2022 +1100

    Merge pull request #341 from mkj/progtools
    
    orangecrab programming targets

"""

# Tool version info
tool_version_str = "0.0.post122"
tool_version_tuple = (0, 0, 122)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post122")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
