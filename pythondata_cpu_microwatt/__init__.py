import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1205"
version_tuple = (0, 0, 1205)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1205")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1079"
data_version_tuple = (0, 0, 1079)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1079")
except ImportError:
    pass
data_git_hash = "ffcdaaa92d3ef4fc8a4c75d0517da02bcdf91a61"
data_git_describe = "v0.0-1079-gffcdaaa"
data_git_msg = """\
commit ffcdaaa92d3ef4fc8a4c75d0517da02bcdf91a61
Author: Michael Neuling <mikey@neuling.org>
Date:   Fri Feb 25 13:18:38 2022 +1100

    Update the README Issues (#350)
    
    We've had these for a while now:
     - D/I cache
     - GPR bypassing
     - Supervisor state (and can boot linux)
    
    We still need Vector/VMX/VSX (and probably some other things)
    
    Signed-off-by: Michael Neuling <mikey@neuling.org>

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
