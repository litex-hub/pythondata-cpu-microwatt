import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1215"
version_tuple = (0, 0, 1215)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1215")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1089"
data_version_tuple = (0, 0, 1089)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1089")
except ImportError:
    pass
data_git_hash = "8bf48ac094ac1f6c01e4c483132645874552c327"
data_git_describe = "v0.0-1089-g8bf48ac"
data_git_msg = """\
commit 8bf48ac094ac1f6c01e4c483132645874552c327
Merge: 30fd936 b5accb7
Author: Michael Neuling <mikey@neuling.org>
Date:   Fri Mar 18 18:28:34 2022 +1100

    Merge pull request #360 from antonblanchard/log2ceil-issue
    
    wishbone_bram_wrapper ram_addr_bits is 1 bit off

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
