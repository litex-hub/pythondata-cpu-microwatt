import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post646"
version_tuple = (0, 0, 646)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post646")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post593"
data_version_tuple = (0, 0, 593)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post593")
except ImportError:
    pass
data_git_hash = "983f4fefe15800e9c235baeae4a99a5b1737e6da"
data_git_describe = "v0.0-593-g983f4fe"
data_git_msg = """\
commit 983f4fefe15800e9c235baeae4a99a5b1737e6da
Merge: 4a4a98d b0e15f2
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Fri Jun 5 13:16:56 2020 +1000

    Merge pull request #191 from ozbenh/litedram
    
    Litedram updates with L2 cache and sim support

"""

# Tool version info
tool_version_str = "0.0.post53"
tool_version_tuple = (0, 0, 53)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post53")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
