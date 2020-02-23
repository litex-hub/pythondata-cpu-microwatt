import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"
git_hash = "44f53f6bdafe85abc4e7ea783b4169629ed7f686"
git_describe = "v0.0-413-g44f53f6"
version_str = "0.0.post413"
version_tuple = (0, 0)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post413")
except ImportError:
    pass