import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post613"
version_tuple = (0, 0, 613)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post613")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post562"
data_version_tuple = (0, 0, 562)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post562")
except ImportError:
    pass
data_git_hash = "cb25167220949530dc5ab7e1a0222c93af2dba96"
data_git_describe = "v0.0-562-gcb25167"
data_git_msg = """\
commit cb25167220949530dc5ab7e1a0222c93af2dba96
Merge: b82d07c 7b14819
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu May 21 12:29:55 2020 +1000

    Merge pull request #180 from antonblanchard/Makefile-rework
    
    Makefile rework

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
