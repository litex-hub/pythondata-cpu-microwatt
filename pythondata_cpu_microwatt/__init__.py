import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post885"
version_tuple = (0, 0, 885)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post885")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post819"
data_version_tuple = (0, 0, 819)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post819")
except ImportError:
    pass
data_git_hash = "16da9b5ba7702e8d34f6354b86b36c7e9bf471ea"
data_git_describe = "v0.0-819-g16da9b5"
data_git_msg = """\
commit 16da9b5ba7702e8d34f6354b86b36c7e9bf471ea
Merge: b60026e 29fabeb
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Dec 1 11:25:08 2020 +1100

    Merge pull request #249 from paulusmack/master
    
    Sundry bug fixes, plus implement mtmsr

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
