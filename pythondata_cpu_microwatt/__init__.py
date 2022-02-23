import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1202"
version_tuple = (0, 0, 1202)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1202")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1076"
data_version_tuple = (0, 0, 1076)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1076")
except ImportError:
    pass
data_git_hash = "2b97fb0bf3d159a125122f8f0bdb5f24ef57e096"
data_git_describe = "v0.0-1076-g2b97fb0"
data_git_msg = """\
commit 2b97fb0bf3d159a125122f8f0bdb5f24ef57e096
Merge: 27b660e 0aa898c
Author: Michael Neuling <mikey@neuling.org>
Date:   Wed Feb 23 12:03:59 2022 +1100

    Merge pull request #348 from paulusmack/reduce
    
    Reduce LUT usage

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
