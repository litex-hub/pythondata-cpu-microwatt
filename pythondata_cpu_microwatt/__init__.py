import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post701"
version_tuple = (0, 0, 701)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post701")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post641"
data_version_tuple = (0, 0, 641)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post641")
except ImportError:
    pass
data_git_hash = "1fedc7a86adedc145c8fab6f8984e38607db8e4a"
data_git_describe = "v0.0-641-g1fedc7a"
data_git_msg = """\
commit 1fedc7a86adedc145c8fab6f8984e38607db8e4a
Merge: 12a257f 67b6117
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Thu Jun 18 07:26:01 2020 +1000

    Merge pull request #207 from ozbenh/misc
    
    Random cleanups of the SoC interfaces

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
