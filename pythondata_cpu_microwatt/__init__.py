import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post996"
version_tuple = (0, 0, 996)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post996")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post901"
data_version_tuple = (0, 0, 901)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post901")
except ImportError:
    pass
data_git_hash = "0af906232f51827d624f570c1dc8eaeee8713725"
data_git_describe = "v0.0-901-g0af9062"
data_git_msg = """\
commit 0af906232f51827d624f570c1dc8eaeee8713725
Merge: 5cc5d8f 4ab3651
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Wed Mar 24 21:31:54 2021 +1100

    Merge pull request #285 from antonblanchard/Makefile-cleanup-2
    
    A few Makefile cleanups

"""

# Tool version info
tool_version_str = "0.0.post95"
tool_version_tuple = (0, 0, 95)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post95")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
