from setuptools import setup, find_packages

setup(
    name="SudsSigner",
    version="2.0.0",
    classifiers=[
        'Private :: Do Not Upload',
    ],
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
