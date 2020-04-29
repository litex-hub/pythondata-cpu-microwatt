import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post511"
version_tuple = (0, 0, 511)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post511")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post461"
data_version_tuple = (0, 0, 461)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post461")
except ImportError:
    pass
data_git_hash = "f21f9dd5a0acbe9215703161f599252f1bf87d80"
data_git_describe = "v0.0-461-gf21f9dd"
data_git_msg = """\
commit f21f9dd5a0acbe9215703161f599252f1bf87d80
Merge: b6bd1ba ff162e4
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu Apr 23 19:50:16 2020 +1000

    Merge pull request #164 from mikey/tags
    
    Add VHDL TAGS

"""

# Tool version info
tool_version_str = "0.0.post50"
tool_version_tuple = (0, 0, 50)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post50")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
