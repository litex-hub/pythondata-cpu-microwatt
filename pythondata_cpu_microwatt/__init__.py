import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post965"
version_tuple = (0, 0, 965)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post965")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post876"
data_version_tuple = (0, 0, 876)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post876")
except ImportError:
    pass
data_git_hash = "9a6a7e9fe5711b0d3fd0b62d98b3f80b9bf6394e"
data_git_describe = "v0.0-876-g9a6a7e9"
data_git_msg = """\
commit 9a6a7e9fe5711b0d3fd0b62d98b3f80b9bf6394e
Merge: 7652452 0fb207b
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Feb 8 16:38:57 2021 +1100

    Merge pull request #268 from paulusmack/btc
    
    Implement branch target cache

"""

# Tool version info
tool_version_str = "0.0.post89"
tool_version_tuple = (0, 0, 89)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post89")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
