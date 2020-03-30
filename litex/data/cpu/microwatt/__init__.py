import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"
git_hash = "8bee4ae3cc629098b13a36a11c97284fc0509bed"
git_describe = "v0.0-426-g8bee4ae"
version_str = "0.0.post426"
version_tuple = (0, 0)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post426")
except ImportError:
    pass
