import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"

# Module version
version_str = "0.0.post474"
version_tuple = (0, 0, 474)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post474")
except ImportError:
    pass

# Data version info
data_version_str = "0.0.post431"
data_version_tuple = (0, 0, 431)
try:
    from packaging.version import Version as V
    pdata_version = V("0.0.post431")
except ImportError:
    pass
data_git_hash = "d3291dbdf01960e900e1d863f02f35a45a611454"
data_git_describe = "v0.0-431-gd3291db"

# Tool version info
tool_version_str = "0.0.post43"
tool_version_tuple = (0, 0, 43)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post43")
except ImportError:
    pass
