import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "vhdl")
src = "https://github.com/antonblanchard/microwatt"
git_hash = "d3291dbdf01960e900e1d863f02f35a45a611454"
git_describe = "v0.0-431-gd3291db"
version_str = "0.0.post431"
version_tuple = (0, 0)
try:
    from packaging.version import Version as V
    pversion = V("0.0.post431")
except ImportError:
    pass
