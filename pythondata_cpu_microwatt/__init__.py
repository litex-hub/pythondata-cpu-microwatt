import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post661"
version_tuple = (0, 0, 661)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post661")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post608"
data_version_tuple = (0, 0, 608)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post608")
except ImportError:
    pass
data_git_hash = "13da4caafb0f652d9f00744a62479a0eab2ccfee"
data_git_describe = "v0.0-608-g13da4ca"
data_git_msg = """\
commit 13da4caafb0f652d9f00744a62479a0eab2ccfee
Merge: 0739b55 097d19f
Author: Michael Neuling <mikey@neuling.org>
Date:   Wed Jun 10 09:54:35 2020 +1000

    Merge pull request #196 from ozbenh/makefile-lib-fix
    
    Makefile: Improve unisim library generation

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
