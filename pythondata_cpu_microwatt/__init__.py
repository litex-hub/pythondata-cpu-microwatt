import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1257"
version_tuple = (0, 0, 1257)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1257")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1115"
data_version_tuple = (0, 0, 1115)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1115")
except ImportError:
    pass
data_git_hash = "ee5e3778edc1d6234195d746236e3804f682a9cf"
data_git_describe = "v0.0-1115-gee5e377"
data_git_msg = """\
commit ee5e3778edc1d6234195d746236e3804f682a9cf
Merge: c43692f 9ec22af
Author: Michael Neuling <mikey@neuling.org>
Date:   Thu Jun 16 14:38:12 2022 +1000

    Merge pull request #364 from shenki/readme-updates
    
    Readme updates

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
