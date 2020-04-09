import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

from pythondata_cpu_microwatt import version_str

setuptools.setup(
    name="pythondata-cpu-microwatt",
    version=version_str,
    author="LiteX Authors",
    author_email="litex@googlegroups.com",
    description="""\
Python module containing vhdl files for microwatt cpu.""",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/litex-hub/pythondata-cpu-microwatt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
    zip_safe=False,
    packages=setuptools.find_packages(),
    package_data={
    	'cpu_microwatt': ['cpu_microwatt/vhdl/**'],
    },
    include_package_data=True,
    project_urls={
        "Bug Tracker": "https://github.com/litex-hub/pythondata-cpu-microwatt/issues",
        "Source Code": "https://github.com/litex-hub/pythondata-cpu-microwatt",
    },
)
