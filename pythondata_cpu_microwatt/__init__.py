import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post888"
version_tuple = (0, 0, 888)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post888")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post822"
data_version_tuple = (0, 0, 822)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post822")
except ImportError:
    pass
data_git_hash = "77c03e5d42d8821b2f8b74bc0fe5cc418b022a10"
data_git_describe = "v0.0-822-g77c03e5"
data_git_msg = """\
commit 77c03e5d42d8821b2f8b74bc0fe5cc418b022a10
Merge: 605010e bc4e6b7
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Dec 7 16:20:09 2020 +1100

    Merge pull request #252 from antonblanchard/hello-world-in-8k
    
    Reduce hello_world footprint to fit in 8kB

"""

# Tool version info
tool_version_str = "0.0.post66"
tool_version_tuple = (0, 0, 66)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post66")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
