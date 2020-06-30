import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post755"
version_tuple = (0, 0, 755)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post755")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post695"
data_version_tuple = (0, 0, 695)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post695")
except ImportError:
    pass
data_git_hash = "ce0205b262f5731900b054dfc43f06f7af14aa98"
data_git_describe = "v0.0-695-gce0205b"
data_git_msg = """\
commit ce0205b262f5731900b054dfc43f06f7af14aa98
Merge: 419c9a6 7406219
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jun 30 15:47:36 2020 +1000

    Merge pull request #216 from paulusmack/cfar
    
    Timing and speed improvements, implement CFAR register

"""

# Tool version info
tool_version_str = "0.0.post60"
tool_version_tuple = (0, 0, 60)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post60")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
