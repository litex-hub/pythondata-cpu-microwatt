import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1409"
version_tuple = (0, 0, 1409)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1409")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1267"
data_version_tuple = (0, 0, 1267)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1267")
except ImportError:
    pass
data_git_hash = "7d928200b81851c6a0ead589297b357dcdf762f2"
data_git_describe = "v0.0-1267-g7d92820"
data_git_msg = """\
commit 7d928200b81851c6a0ead589297b357dcdf762f2
Merge: 964b97e d299ea9
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Oct 25 10:52:34 2022 +1100

    Merge pull request #415 from ozbenh/uart16550-core
    
    Bundle the uart16550 core file

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
