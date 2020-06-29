import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post748"
version_tuple = (0, 0, 748)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post748")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post688"
data_version_tuple = (0, 0, 688)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post688")
except ImportError:
    pass
data_git_hash = "57604c1a6e3a5315f61db074c42ad2063a799246"
data_git_describe = "v0.0-688-g57604c1"
data_git_msg = """\
commit 57604c1a6e3a5315f61db074c42ad2063a799246
Merge: 9bbef03 434962b
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Jun 29 12:19:06 2020 +1000

    Merge pull request #213 from ozbenh/uart16550
    
    Add support for standard 16550 style UART

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
