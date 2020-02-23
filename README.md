# litex-data-cpu-microwatt

Non-Python data files required to use the microwatt with
[LiteX](https://github.com/enjoy-digital/litex.git).

The data files can be found under the Python module `litex.data.cpu.microwatt`. The
`litex.data.cpu.microwatt.location` value can be used to find the files on the file system.
For example;

```python
import litex.data.cpu.microwatt

my_data_file = "abc.txt"

with open(os.path.join(litex.data.cpu.microwatt.location, my_data_file)) as f:
    print(f.read())
```

The data files come from https://github.com/antonblanchard/microwatt
and are imported using `git subtrees` to the directory
[litex/data/cpu/microwatt/vhdl](litex/data/cpu/microwatt/vhdl].

## Installing

## Manually

You can install the package manually, however this is **not** recommended.

```
git clone https://github.com/litex-hub/litex-data-cpu-microwatt.git
cd litex-data-cpu-microwatt
sudo python setup.py install
```

## Using [pip](https://pip.pypa.io/)

You can use [pip](https://pip.pypa.io/) to install the data package directly
from github using;

```
pip install --user git+https://github.com/litex-hub/litex-data-cpu-microwatt.git
```

If you want to install for the whole system rather than just the current user,
you need to remove the `--user` argument and run as sudo like so;

```
sudo pip install git+https://github.com/litex-hub/litex-data-cpu-microwatt.git
```

You can install a specific revision of the repository using;
```
pip install --user git+https://github.com/litex-hub/litex-data-cpu-microwatt.git@<tag>
pip install --user git+https://github.com/litex-hub/litex-data-cpu-microwatt.git@<branch>
pip install --user git+https://github.com/litex-hub/litex-data-cpu-microwatt.git@<hash>
```

### With `requirements.txt` file

Add to your Python `requirements.txt` file using;
```
-e git+https://github.com/litex-hub/litex-data-cpu-microwatt.git
```

To use a specific revision of the repository, use the following;
```
-e https://github.com/litex-hub/litex-data-cpu-microwatt.git@<hash>
```