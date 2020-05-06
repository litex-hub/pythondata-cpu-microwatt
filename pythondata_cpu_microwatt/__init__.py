import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post519"
version_tuple = (0, 0, 519)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post519")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post468"
data_version_tuple = (0, 0, 468)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post468")
except ImportError:
    pass
data_git_hash = "4160f2138d348a368cf6bc9b53ce450f7e6de32c"
data_git_describe = "v0.0-468-g4160f21"
data_git_msg = """\
commit 4160f2138d348a368cf6bc9b53ce450f7e6de32c
Merge: 098c3fb 0076f8b
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Wed May 6 13:27:17 2020 +1000

    Merge pull request #165 from mikey/xics
    
    Implement XICS compliant interrupt controller

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
