import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='datas',
    version='0.1',
    scripts=['datas'],
    author="Robert Grzelka",
    author_email="robert.grzelka@outlook.com",
    description="Collection of data structures and algorithms in python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/robgrzel/datas",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 2-Clause 'Simplified' License",
        "Operating System :: OS Independent",
    ],
)
