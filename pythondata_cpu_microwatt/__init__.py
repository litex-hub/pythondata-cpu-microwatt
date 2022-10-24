import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1403"
version_tuple = (0, 0, 1403)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1403")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1261"
data_version_tuple = (0, 0, 1261)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1261")
except ImportError:
    pass
data_git_hash = "432d9f31500e973d44ce8f261c2a82248ad24e24"
data_git_describe = "v0.0-1261-g432d9f3"
data_git_msg = """\
commit 432d9f31500e973d44ce8f261c2a82248ad24e24
Merge: 413f2dc 3f788e8
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Oct 24 15:02:33 2022 +1100

    Merge pull request #413 from ozbenh/fix-io-bridge-qw-store
    
    soc: Fix issues with 64-bit stores to IO bridge

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
