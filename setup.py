from setuptools import setup,find_packages
from pathlib import Path

HYFEN_E_DOT = '-e .'

def get_requirements(file_path:str)->list[str]:
    requiremnets = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n",'') for req in requirements]

        if HYFEN_E_DOT in requirements:
            requirements.remove(HYFEN_E_DOT)

    return requirements


setup(name='mlproject',
      author_email='krunalparekh654@gmail.com',
      author='krunal parekh',
      verion= '0.0.1',
      packages=find_packages(),
      install_requires = get_requirements('requirements.txt')
      )