import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post506"
version_tuple = (0, 0, 506)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post506")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post457"
data_version_tuple = (0, 0, 457)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post457")
except ImportError:
    pass
data_git_hash = "2b11c81b18b214e33d024c83bf91a6b346cfcd11"
data_git_describe = "v0.0-457-g2b11c81"
data_git_msg = """\
commit 2b11c81b18b214e33d024c83bf91a6b346cfcd11
Merge: 4c2bd76 05f4f68
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu Apr 16 18:42:42 2020 +1000

    Merge pull request #162 from antonblanchard/bin2hex-removal
    
    rust_lib_demo: Remove bin2hex.py

"""

# Tool version info
tool_version_str = "0.0.post49"
tool_version_tuple = (0, 0, 49)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post49")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
