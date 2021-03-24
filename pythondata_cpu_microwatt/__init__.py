import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post992"
version_tuple = (0, 0, 992)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post992")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post897"
data_version_tuple = (0, 0, 897)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post897")
except ImportError:
    pass
data_git_hash = "5cc5d8f030d303a82ed38f3b359921a748b746ba"
data_git_describe = "v0.0-897-g5cc5d8f"
data_git_msg = """\
commit 5cc5d8f030d303a82ed38f3b359921a748b746ba
Merge: ef01fa3 2d21b95
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Wed Mar 24 20:44:45 2021 +1100

    Merge pull request #281 from antonblanchard/cache-tlb-parameters
    
    Pass icache/dcache/tlb parameters down from soc

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
