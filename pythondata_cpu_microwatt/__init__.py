import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post624"
version_tuple = (0, 0, 624)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post624")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post571"
data_version_tuple = (0, 0, 571)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post571")
except ImportError:
    pass
data_git_hash = "84ab28b3d28bcfa597aec7ae6d206b2397737baf"
data_git_describe = "v0.0-571-g84ab28b"
data_git_msg = """\
commit 84ab28b3d28bcfa597aec7ae6d206b2397737baf
Merge: 4c1a731 12f36b4
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Tue Jun 2 11:54:00 2020 +1000

    Merge pull request #178 from antonblanchard/intercon
    
    Interconnect timing improvements from Ben

"""

# Tool version info
tool_version_str = "0.0.post53"
tool_version_tuple = (0, 0, 53)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post53")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
