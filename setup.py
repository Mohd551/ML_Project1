from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    """
    Reads the requirements file and returns a list of dependencies.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements if req.strip() and not req.startswith("#")]
    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Suhail',
    author_email='suhail.ansari248@hotmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirments.txt')  
)
