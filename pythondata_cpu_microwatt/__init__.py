import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1207"
version_tuple = (0, 0, 1207)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1207")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1081"
data_version_tuple = (0, 0, 1081)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1081")
except ImportError:
    pass
data_git_hash = "f01f3d233ae4de595fa29beb305d00ce960f041e"
data_git_describe = "v0.0-1081-gf01f3d2"
data_git_msg = """\
commit f01f3d233ae4de595fa29beb305d00ce960f041e
Merge: ffcdaaa c0c00d0
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Feb 28 08:17:50 2022 +1100

    Merge pull request #352 from mkj/static-urjtag
    
    mw_debug: Add STATIC_URJTAG flag

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
