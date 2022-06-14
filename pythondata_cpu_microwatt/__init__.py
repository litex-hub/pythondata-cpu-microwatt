import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1244"
version_tuple = (0, 0, 1244)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1244")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1102"
data_version_tuple = (0, 0, 1102)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1102")
except ImportError:
    pass
data_git_hash = "b82eea593341c3a8da0f0afbd4e8aabdc852ef6d"
data_git_describe = "v0.0-1102-gb82eea5"
data_git_msg = """\
commit b82eea593341c3a8da0f0afbd4e8aabdc852ef6d
Merge: d3aff67 ff442d1
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Jun 14 13:09:57 2022 +1000

    Merge pull request #366 from antonblanchard/hello-world-bss
    
    Zero BSS in hello world test

"""

# Tool version info
tool_version_str = "0.0.post142"
tool_version_tuple = (0, 0, 142)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post142")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_microwatt."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_microwatt".format(f))
    return fn
