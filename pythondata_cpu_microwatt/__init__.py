import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1265"
version_tuple = (0, 0, 1265)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1265")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1123"
data_version_tuple = (0, 0, 1123)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1123")
except ImportError:
    pass
data_git_hash = "35e0dbed345011bafb651fa7d168de550e6fd6e7"
data_git_describe = "v0.0-1123-g35e0dbe"
data_git_msg = """\
commit 35e0dbed345011bafb651fa7d168de550e6fd6e7
Merge: cd52390 844ca0e
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Fri Jun 17 09:46:57 2022 +1000

    Merge pull request #353 from tianrui-wei/master
    
    fix: fix icache_tb not finishing correctly

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
