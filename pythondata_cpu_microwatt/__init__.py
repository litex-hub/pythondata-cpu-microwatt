import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1388"
version_tuple = (0, 0, 1388)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1388")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1246"
data_version_tuple = (0, 0, 1246)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1246")
except ImportError:
    pass
data_git_hash = "d3fb2639dd375fb65a3cce20e44fba2bf28b443d"
data_git_describe = "v0.0-1246-gd3fb263"
data_git_msg = """\
commit d3fb2639dd375fb65a3cce20e44fba2bf28b443d
Merge: 047f739 24d04ed
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Wed Sep 7 18:00:11 2022 +1000

    Merge pull request #403 from mikey/litedram-warnings
    
    Fix litedram wrapper build warnings and metavalues

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
