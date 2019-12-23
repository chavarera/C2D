import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="C2D", # Replace with your own username
    version="0.0.1",
    author="Ravishankar Chavare",
    author_email="chavare.ravi123@gmail.com",
    description="optimal solution to read and save a config file.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chavarera/C2D",
    packages=setuptools.find_packages(),
    classifiers=[
        "Natural Language :: English",
        "Programming Language :: Python :: 3.6",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords=["c2d", "config", "config-parser", "config-reader"],
)
