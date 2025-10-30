from setuptools import setup, find_packages

setup(
    name="pyspark_project",
    version="1.0.0",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'etl_job = etl_job:main',
        ],
    },
    install_requires=[
        "pyspark>=3.0.0",
    ],
)
