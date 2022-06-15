import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1248"
version_tuple = (0, 0, 1248)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1248")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1106"
data_version_tuple = (0, 0, 1106)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1106")
except ImportError:
    pass
data_git_hash = "6e1e763c025fb72707275f1aca0bb55fb9fc2f0d"
data_git_describe = "v0.0-1106-g6e1e763"
data_git_msg = """\
commit 6e1e763c025fb72707275f1aca0bb55fb9fc2f0d
Merge: 1047239 f06abb6
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Wed Jun 15 11:02:58 2022 +1000

    Merge pull request #368 from antonblanchard/icache-pmu-events
    
    icache: Hook up PMU events

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
