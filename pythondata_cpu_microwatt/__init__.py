import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post617"
version_tuple = (0, 0, 617)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post617")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post564"
data_version_tuple = (0, 0, 564)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post564")
except ImportError:
    pass
data_git_hash = "bdb428a40bfa1e9a374c816cdf3da67315be5ad2"
data_git_describe = "v0.0-564-gbdb428a"
data_git_msg = """\
commit bdb428a40bfa1e9a374c816cdf3da67315be5ad2
Merge: cb25167 04c56a0
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Sat May 23 16:50:12 2020 +1000

    Merge pull request #181 from antonblanchard/Makefile-rework-2
    
    Pass clock frequency to UART sim wrapper

"""

# Tool version info
tool_version_str = "0.0.post53"
tool_version_tuple = (0, 0, 53)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post53")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
