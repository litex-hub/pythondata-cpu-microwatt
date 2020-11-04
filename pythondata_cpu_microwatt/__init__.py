import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post873"
version_tuple = (0, 0, 873)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post873")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post807"
data_version_tuple = (0, 0, 807)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post807")
except ImportError:
    pass
data_git_hash = "e40e752b9ab602f5ce1eb79be1fe96932558830d"
data_git_describe = "v0.0-807-ge40e752"
data_git_msg = """\
commit e40e752b9ab602f5ce1eb79be1fe96932558830d
Merge: 168d30c 73f8193
Author: Michael Neuling <mikey@neuling.org>
Date:   Thu Sep 17 12:04:26 2020 +1000

    Merge pull request #245 from paulusmack/fpu
    
    Add a simple FPU

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
