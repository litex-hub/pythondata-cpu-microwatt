import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1261"
version_tuple = (0, 0, 1261)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1261")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1119"
data_version_tuple = (0, 0, 1119)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1119")
except ImportError:
    pass
data_git_hash = "b983d5080e27a267ff349635289103b74058df1e"
data_git_describe = "v0.0-1119-gb983d50"
data_git_msg = """\
commit b983d5080e27a267ff349635289103b74058df1e
Merge: d4db331 b47b718
Author: Michael Neuling <mikey@neuling.org>
Date:   Thu Jun 16 16:47:33 2022 +1000

    Merge pull request #376 from antonblanchard/loadstore-init
    
    loadstore1: reduce U state being output

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
