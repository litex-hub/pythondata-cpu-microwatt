import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post485"
version_tuple = (0, 0, 485)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post485")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post436"
data_version_tuple = (0, 0, 436)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post436")
except ImportError:
    pass
data_git_hash = "e8a55f900fdce81fc62d261a197eb028f38b211f"
data_git_describe = "v0.0-436-ge8a55f9"
data_git_msg = """\
commit e8a55f900fdce81fc62d261a197eb028f38b211f
Merge: d3291db e990e9c
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu Apr 9 11:47:05 2020 +1000

    Merge pull request #157 from paulusmack/master
    
    Start using cache-inhibited loads and stores to access the UART

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
