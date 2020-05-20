import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post606"
version_tuple = (0, 0, 606)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post606")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post555"
data_version_tuple = (0, 0, 555)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post555")
except ImportError:
    pass
data_git_hash = "b82d07c8d569494721043d4a9d6d93a22590f335"
data_git_describe = "v0.0-555-gb82d07c"
data_git_msg = """\
commit b82d07c8d569494721043d4a9d6d93a22590f335
Merge: 354e0fb 8c028f2
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue May 19 15:53:54 2020 +1000

    Merge pull request #179 from antonblanchard/yosys-verilator
    
    Add yosys/verilator support

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
