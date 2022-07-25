import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1268"
version_tuple = (0, 0, 1268)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1268")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1126"
data_version_tuple = (0, 0, 1126)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1126")
except ImportError:
    pass
data_git_hash = "bad9a9a2e815c252ec984dd0b747f1dc888c863c"
data_git_describe = "v0.0-1126-gbad9a9a"
data_git_msg = """\
commit bad9a9a2e815c252ec984dd0b747f1dc888c863c
Merge: 35e0dbe a060ad5
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Jul 25 16:31:12 2022 +1000

    Merge pull request #380 from iagocaran/master
    
    tests/pmu: Add load/store completed and instruction/cycle count

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
