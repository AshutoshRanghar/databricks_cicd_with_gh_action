from setuptools import setup, find_packages

setup(
    name="pyspark_project",
    version="1.0.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "pyspark>=3.3.0",
    ],
)
