import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post627"
version_tuple = (0, 0, 627)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post627")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post574"
data_version_tuple = (0, 0, 574)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post574")
except ImportError:
    pass
data_git_hash = "62233eddd7fcc9284650e201fa216fa0788d631e"
data_git_describe = "v0.0-574-g62233ed"
data_git_msg = """\
commit 62233eddd7fcc9284650e201fa216fa0788d631e
Merge: 84ab28b 60d2b8a
Author: Paul Mackerras <paulus@ozlabs.org>
Date:   Wed Jun 3 14:20:02 2020 +1000

    Merge pull request #168 from shenki/flash-arty
    
    Scripts to write data to the Arty's SPI flash

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
