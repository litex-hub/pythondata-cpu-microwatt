import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post514"
version_tuple = (0, 0, 514)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post514")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post463"
data_version_tuple = (0, 0, 463)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post463")
except ImportError:
    pass
data_git_hash = "098c3fbb2bd0a750475c91128d293b03adde5aa5"
data_git_describe = "v0.0-463-g098c3fb"
data_git_msg = """\
commit 098c3fbb2bd0a750475c91128d293b03adde5aa5
Merge: f21f9dd c818853
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Fri May 1 19:52:59 2020 +1000

    Merge pull request #167 from tomtor/patch-1
    
    Fix Rust README.md

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
