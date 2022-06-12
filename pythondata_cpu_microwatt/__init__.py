import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1240"
version_tuple = (0, 0, 1240)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1240")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1098"
data_version_tuple = (0, 0, 1098)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1098")
except ImportError:
    pass
data_git_hash = "1ff852b012155ad610e9d044cac3461adc198f85"
data_git_describe = "v0.0-1098-g1ff852b"
data_git_msg = """\
commit 1ff852b012155ad610e9d044cac3461adc198f85
Merge: b7c4d3c e243807
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Sun Jun 12 10:24:54 2022 +1000

    Merge pull request #369 from antonblanchard/loadstore-pmu-init
    
    loadstore1: Initialise PMU events

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
