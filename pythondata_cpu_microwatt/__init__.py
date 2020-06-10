import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post674"
version_tuple = (0, 0, 674)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post674")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post614"
data_version_tuple = (0, 0, 614)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post614")
except ImportError:
    pass
data_git_hash = "6bb3837b332891d8414cfc80ad28b0b5585dd5e3"
data_git_describe = "v0.0-614-g6bb3837"
data_git_msg = """\
commit 6bb3837b332891d8414cfc80ad28b0b5585dd5e3
Merge: 13da4ca 183d05d
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Wed Jun 10 19:37:01 2020 +1000

    Merge pull request #194 from ozbenh/misc
    
    Fix syscon registers usage and add "save" function to mw_debug

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
