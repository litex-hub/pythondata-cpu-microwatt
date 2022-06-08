import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1236"
version_tuple = (0, 0, 1236)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1236")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1094"
data_version_tuple = (0, 0, 1094)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1094")
except ImportError:
    pass
data_git_hash = "b8fc5636a4e811701508499c67bf8e4d7b390c33"
data_git_describe = "v0.0-1094-gb8fc563"
data_git_msg = """\
commit b8fc5636a4e811701508499c67bf8e4d7b390c33
Merge: f5e06c2 ebdddcc
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Wed Jun 8 14:54:48 2022 +1000

    Merge pull request #365 from antonblanchard/less-fpga-init
    
    Remove some FPGA style signal inits

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
