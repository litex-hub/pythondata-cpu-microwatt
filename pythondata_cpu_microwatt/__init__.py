import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1194"
version_tuple = (0, 0, 1194)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1194")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1070"
data_version_tuple = (0, 0, 1070)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1070")
except ImportError:
    pass
data_git_hash = "27b660ef769a61ff1afc567d108438222803fd16"
data_git_describe = "v0.0-1070-g27b660e"
data_git_msg = """\
commit 27b660ef769a61ff1afc567d108438222803fd16
Merge: 5a5a082 9c64f8a
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Feb 8 09:09:22 2022 +1100

    Merge pull request #346 from mkj/dmi_ecp5
    
    Add DMI and mw_debug for ECP5

"""

# Tool version info
tool_version_str = "0.0.post124"
tool_version_tuple = (0, 0, 124)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post124")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
