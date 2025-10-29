from setuptools import setup, find_packages

setup(
    name='pyspark_project',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pyspark>=3.3.0',
        'delta-spark>=2.4.0'
    ],
    entry_points={
        'console_scripts': [
            'run-etl=pyspark_project.etl_job:main'
        ]
    }
)
