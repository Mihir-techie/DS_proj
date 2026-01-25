from setuptools import setup, find_packages
from pathlib import Path
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file:
        requirements = file.readlines()
        requirements = [req.strip() for req in requirements]
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
            return requirements
        return requirements
    
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()
setup(
    name="production_ml_project",
    version="0.1.0",
    author="Mihir Kumar Panigrahi",
    author_email="mihirkumarpanigrahi2002@gmail.com",
    description="A Production Machine Learning Project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mihir-techie/DS_proj.git",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scikit-learn",
        "seaborn",
        "requests",
        "flask"


    ]


)








