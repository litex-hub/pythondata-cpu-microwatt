import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1398"
version_tuple = (0, 0, 1398)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1398")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1256"
data_version_tuple = (0, 0, 1256)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1256")
except ImportError:
    pass
data_git_hash = "84a0fba25de23cc7bdd1e20918c4615a2a2e00cb"
data_git_describe = "v0.0-1256-g84a0fba"
data_git_msg = """\
commit 84a0fba25de23cc7bdd1e20918c4615a2a2e00cb
Merge: 5766dba b8f9c83
Author: Michael Neuling <mikey@neuling.org>
Date:   Thu Sep 29 11:49:08 2022 +1000

    Merge pull request #408 from paulusmack/plru-improvement
    
    PLRU improvements

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
