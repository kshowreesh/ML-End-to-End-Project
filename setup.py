from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """Return list of requirements from a file."""
    with open(file_path) as file_obj:
        requirements = [line.strip() for line in file_obj]

    if HYPEN_E_DOT in requirements:
        requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name='ml_end_to_end_project',
    version='0.0.1',
    author='kulashowreesh',
    author_email='kshowreesh@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)


