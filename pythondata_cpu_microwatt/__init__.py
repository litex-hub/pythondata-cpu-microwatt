import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post1407"
version_tuple = (0, 0, 1407)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post1407")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post1265"
data_version_tuple = (0, 0, 1265)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post1265")
except ImportError:
    pass
data_git_hash = "964b97e85cd60cdac29553cd308854a505f0404b"
data_git_describe = "v0.0-1265-g964b97e"
data_git_msg = """\
commit 964b97e85cd60cdac29553cd308854a505f0404b
Merge: 432d9f3 6068b63
Author: Michael Neuling <mikey@neuling.org>
Date:   Tue Oct 25 09:02:08 2022 +1100

    Merge pull request #414 from ozbenh/misc
    
    Fixup plru_tb to use the new plrufn, take out the old plru and vunit test misc changes

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
