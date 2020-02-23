import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from litex.data.cpu.microwatt import version_str

setuptools.setup(
    name="litex-data-cpu-microwatt",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="Python module containing data files for using the microwatt cpu with LiteX.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/litex-data-cpu-microwatt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Creative Commons Attribution-ShareAlike 4.0 License (CC-BY-SA 4.0)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={'litex.data.cpu.microwatt': ['litex/data/cpu/microwatt/vhdl/**']},
    include_package_data=True,
)