import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post694"
version_tuple = (0, 0, 694)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post694")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post634"
data_version_tuple = (0, 0, 634)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post634")
except ImportError:
    pass
data_git_hash = "12a257f01edb3c1d8986e89e6750d4a1f69822f4"
data_git_describe = "v0.0-634-g12a257f"
data_git_msg = """\
commit 12a257f01edb3c1d8986e89e6750d4a1f69822f4
Merge: bf6cc2a 176ae5c
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Sat Jun 13 12:36:16 2020 +1000

    Merge pull request #205 from ozbenh/timing
    
    Timing improvements

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
