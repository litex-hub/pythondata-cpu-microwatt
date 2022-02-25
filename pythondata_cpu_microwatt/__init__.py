import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1204"
version_tuple = (0, 0, 1204)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1204")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1078"
data_version_tuple = (0, 0, 1078)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1078")
except ImportError:
    pass
data_git_hash = "b4770197a2e07c321f283d8882a3dcb380a1344b"
data_git_describe = "v0.0-1078-gb477019"
data_git_msg = """\
commit b4770197a2e07c321f283d8882a3dcb380a1344b
Merge: 2b97fb0 fcb783a
Author: Michael Neuling <mikey@neuling.org>
Date:   Fri Feb 25 11:08:57 2022 +1100

    Merge pull request #349 from madscientist159/master
    
    Extend LiteDRAM VHDL wrapper to allow more than one clock line

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
