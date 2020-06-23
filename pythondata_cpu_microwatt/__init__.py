import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post731"
version_tuple = (0, 0, 731)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post731")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post671"
data_version_tuple = (0, 0, 671)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post671")
except ImportError:
    pass
data_git_hash = "695e081c35792e9db7e14da206e1410dc4a8e6b9"
data_git_describe = "v0.0-671-g695e081"
data_git_msg = """\
commit 695e081c35792e9db7e14da206e1410dc4a8e6b9
Merge: b90a0a2 bb54af5
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jun 23 14:32:42 2020 +1000

    Merge pull request #210 from ozbenh/xics
    
    xics: Cleanups and add a simple ICS for use by Linux

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
