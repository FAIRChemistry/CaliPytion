import setuptools
from setuptools import setup

setup(
    name="CaliPytion",
    version="0.0.3",
    description="Data model and standard curve functionalities for calibration data",
    url="https://github.com/FAIRChemistry/calibration_data",
    author="Haeussler, Max",
    author_email="st171427@stud.uni-stuttgart.de",
    packages=setuptools.find_packages(),
    install_requires=[
        "lmfit",
        "matplotlib",
        "numpy",
        "pandas",
        "pydantic==1.8.2",
        "scipy",
        "setuptools"]
    )
