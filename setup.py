from setuptools import setup, find_packages

setup(
    name="PythonParser",
    description="Python Parser using PLY",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["ply", "rich"],
    author="Kavin S, M V Chinmay",
)
