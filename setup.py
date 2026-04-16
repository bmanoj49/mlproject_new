## setup.py file will be responsible for creating the machine learning project as a package.

from setuptools import find_packages,setup
from typing import List


HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)-> List[str]:
    '''
    This fucntion will return list of requirements'''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name='mlproject_new',
    version='0.0.1',
    author='Manoj',
    author_email='bmanoj49@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)