import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1299"
version_tuple = (0, 0, 1299)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1299")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1157"
data_version_tuple = (0, 0, 1157)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1157")
except ImportError:
    pass
data_git_hash = "281a125f1fa9edb464dd580874899d2732a92d0f"
data_git_describe = "v0.0-1157-g281a125"
data_git_msg = """\
commit 281a125f1fa9edb464dd580874899d2732a92d0f
Merge: bad9a9a d6121cd
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jul 26 10:08:33 2022 +1000

    Merge pull request #379 from paulusmack/master
    
    Lots of improvements

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
