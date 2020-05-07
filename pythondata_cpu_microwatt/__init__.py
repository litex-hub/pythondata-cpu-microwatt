import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post531"
version_tuple = (0, 0, 531)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post531")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post480"
data_version_tuple = (0, 0, 480)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post480")
except ImportError:
    pass
data_git_hash = "1ba29a407a223466ff959bd88c4a91e1f85ff622"
data_git_describe = "v0.0-480-g1ba29a4"
data_git_msg = """\
commit 1ba29a407a223466ff959bd88c4a91e1f85ff622
Merge: 4160f21 102fbcf
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu May 7 09:59:19 2020 +1000

    Merge pull request #166 from paulusmack/master
    
    MSR fixes, implement privilege checking, implement dcbz

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
