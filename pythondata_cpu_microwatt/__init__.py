import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1152"
version_tuple = (0, 0, 1152)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1152")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1040"
data_version_tuple = (0, 0, 1040)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1040")
except ImportError:
    pass
data_git_hash = "7fa7b45faa17950de44591f7a73722fdf8a87385"
data_git_describe = "v0.0-1040-g7fa7b45"
data_git_msg = """\
commit 7fa7b45faa17950de44591f7a73722fdf8a87385
Merge: 8a03050 d458b58
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Oct 25 16:49:19 2021 +1100

    Merge pull request #337 from paulusmack/fixes
    
    ECP5: Adjust PLL constants so the PLL lock indication works

"""

# Tool version info
tool_version_str = "0.0.post112"
tool_version_tuple = (0, 0, 112)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post112")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
