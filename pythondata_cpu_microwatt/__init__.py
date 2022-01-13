import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1164"
version_tuple = (0, 0, 1164)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1164")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1042"
data_version_tuple = (0, 0, 1042)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1042")
except ImportError:
    pass
data_git_hash = "67164a6ffa41672d8779f62efb0a5a7d96b7a1f7"
data_git_describe = "v0.0-1042-g67164a6"
data_git_msg = """\
commit 67164a6ffa41672d8779f62efb0a5a7d96b7a1f7
Merge: 7fa7b45 9ceb463
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Sun Jan 9 08:08:48 2022 +1100

    Merge pull request #338 from shenki/yosys-read-verilog
    
    Makefile: Use read_verilog with yosys

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
