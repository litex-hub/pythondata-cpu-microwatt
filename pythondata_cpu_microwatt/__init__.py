import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1213"
version_tuple = (0, 0, 1213)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1213")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1087"
data_version_tuple = (0, 0, 1087)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1087")
except ImportError:
    pass
data_git_hash = "30fd936c128c83391ad358d0aae8e958bd124399"
data_git_describe = "v0.0-1087-g30fd936"
data_git_msg = """\
commit 30fd936c128c83391ad358d0aae8e958bd124399
Merge: af1b76d 0b39947
Author: Michael Neuling <mikey@neuling.org>
Date:   Wed Mar 16 10:49:47 2022 +1100

    Merge pull request #358 from antonblanchard/unused-sig
    
    Remove unused sequential signal from Fetch1ToIcacheType

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
