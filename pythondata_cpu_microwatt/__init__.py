import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post979"
version_tuple = (0, 0, 979)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post979")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post890"
data_version_tuple = (0, 0, 890)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post890")
except ImportError:
    pass
data_git_hash = "6c7689052dbd76b5fe7c9f4804d6a4817e9845af"
data_git_describe = "v0.0-890-g6c76890"
data_git_msg = """\
commit 6c7689052dbd76b5fe7c9f4804d6a4817e9845af
Merge: 9a6a7e9 17fd069
Author: Michael Neuling <mikey@neuling.org>
Date:   Mon Feb 8 17:27:16 2021 +1100

    Merge pull request #269 from paulusmack/pipeline
    
    Rework load/store pipeline to achieve one load/store per cycle throughput

"""

# Tool version info
tool_version_str = "0.0.post89"
tool_version_tuple = (0, 0, 89)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post89")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
