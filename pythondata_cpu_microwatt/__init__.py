import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1227"
version_tuple = (0, 0, 1227)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1227")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1091"
data_version_tuple = (0, 0, 1091)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1091")
except ImportError:
    pass
data_git_hash = "f5e06c2d4bd8faa90a2d3c47ca7ba22343e3aae8"
data_git_describe = "v0.0-1091-gf5e06c2"
data_git_msg = """\
commit f5e06c2d4bd8faa90a2d3c47ca7ba22343e3aae8
Merge: 8bf48ac 948f6f4
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Mar 22 11:55:54 2022 +1100

    Merge pull request #361 from antonblanchard/alt-reset-address
    
    Allow ALT_RESET_ADDRESS to be overridden

"""

# Tool version info
tool_version_str = "0.0.post136"
tool_version_tuple = (0, 0, 136)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post136")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
