import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post548"
version_tuple = (0, 0, 548)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post548")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post497"
data_version_tuple = (0, 0, 497)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post497")
except ImportError:
    pass
data_git_hash = "fcec66acf4dc9b4b5480bf18a118a42ec87c7eba"
data_git_describe = "v0.0-497-gfcec66a"
data_git_msg = """\
commit fcec66acf4dc9b4b5480bf18a118a42ec87c7eba
Merge: 1ba29a4 e3013f5
Author: Anton Blanchard <anton@linux.ibm.com>
Date:   Thu May 14 15:08:33 2020 +1000

    Merge pull request #170 from antonblanchard/litedram
    
    LiteDRAM integration

"""

# Tool version info
tool_version_str = "0.0.post51"
tool_version_tuple = (0, 0, 51)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post51")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
