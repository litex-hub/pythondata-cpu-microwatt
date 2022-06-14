import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1246"
version_tuple = (0, 0, 1246)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1246")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1104"
data_version_tuple = (0, 0, 1104)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1104")
except ImportError:
    pass
data_git_hash = "1047239a377304f25095eb179de9c06977a5e732"
data_git_describe = "v0.0-1104-g1047239"
data_git_msg = """\
commit 1047239a377304f25095eb179de9c06977a5e732
Merge: b82eea5 9d35340
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue Jun 14 18:10:37 2022 +1000

    Merge pull request #377 from antonblanchard/fpu-init
    
    fpu: Reduce uninitialised signals

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
