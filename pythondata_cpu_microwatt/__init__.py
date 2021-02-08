import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post955"
version_tuple = (0, 0, 955)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post955")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post866"
data_version_tuple = (0, 0, 866)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post866")
except ImportError:
    pass
data_git_hash = "7652452367c634e85146d565fd6296572ce77c11"
data_git_describe = "v0.0-866-g7652452"
data_git_msg = """\
commit 7652452367c634e85146d565fd6296572ce77c11
Merge: c4e3ade 481f3cd
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Feb 8 14:34:53 2021 +1100

    Merge pull request #273 from antonblanchard/wishbone-checking
    
    Add some wishbone checking

"""

# Tool version info
tool_version_str = "0.0.post89"
tool_version_tuple = (0, 0, 89)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post89")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
