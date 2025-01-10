from setuptools import setup, find_packages

setup(
    name="Python203",
    version="0.1",
    packages=find_packages(where="src"),  # Search for packages in the "src" directory
    package_dir={"": "src"},             # Root of packages is "src"
    include_package_data=True,           # Include non-Python files
    python_requires=">=3.7",             # Minimum Python version
)
