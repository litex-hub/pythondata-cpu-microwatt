import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post733"
version_tuple = (0, 0, 733)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post733")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post673"
data_version_tuple = (0, 0, 673)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post673")
except ImportError:
    pass
data_git_hash = "7566f04fe3f0807cde42b1965feae57fe4346476"
data_git_describe = "v0.0-673-g7566f04"
data_git_msg = """\
commit 7566f04fe3f0807cde42b1965feae57fe4346476
Merge: 695e081 60e5f7b
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jun 23 16:58:06 2020 +1000

    Merge pull request #211 from shenki/spi-constraint
    
    spi: Fix dat_i_l constraints

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
