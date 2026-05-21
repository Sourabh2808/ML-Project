from setuptools import setup, find_packages
from typing import List

#HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:

    requirements=[]

    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','') for req in requirements]

    #if HYPEN_E_DOT in requirements:   <= this is when we have -e . in requirements.txt file, which is not needed for installation and creates error, so we will remove it from the list of requirementsi
    #    requirements.remove(HYPEN_E_DOT)

    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='Sourabh',
    author_email='sourabhkarajage@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)