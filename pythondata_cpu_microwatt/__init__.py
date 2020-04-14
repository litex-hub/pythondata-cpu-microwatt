import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post495"
version_tuple = (0, 0, 495)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post495")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post446"
data_version_tuple = (0, 0, 446)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post446")
except ImportError:
    pass
data_git_hash = "97e3d47a13d332e0eb25fea9e8167b7c575f467d"
data_git_describe = "v0.0-446-g97e3d47"
data_git_msg = """\
commit 97e3d47a13d332e0eb25fea9e8167b7c575f467d
Merge: e8a55f9 5657782
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue Apr 14 12:47:00 2020 +1000

    Merge pull request #158 from paulusmack/excpath
    
    Fix exception stuff so we make timing again

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
