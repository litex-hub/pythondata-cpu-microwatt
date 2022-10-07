import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1401"
version_tuple = (0, 0, 1401)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1401")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1259"
data_version_tuple = (0, 0, 1259)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1259")
except ImportError:
    pass
data_git_hash = "413f2dc5d6094be1ae14fb0c1b0cf19cb08bda25"
data_git_describe = "v0.0-1259-g413f2dc"
data_git_msg = """\
commit 413f2dc5d6094be1ae14fb0c1b0cf19cb08bda25
Merge: 84a0fba 76f61ef
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Fri Oct 7 18:27:13 2022 +1100

    Merge pull request #411 from ozbenh/dcache-plru-update-fix
    
    Dcache PLRU update fix

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
