import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"
git_hash = "cc20989bdab42702be37b547c74bfa55962df34d"
git_describe = "v0.0-415-gcc20989"
version_str = "0.0.post415"
version_tuple = (0, 0)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post415")
except ImportError:
    pass
