import setuptools

__version__ = "0.0.0"

REPO_NAME = "Chest-Cancer-Classification-Project"
AUTHOR_USER_NAME = "Karan"
SRC_REPO = "cnnClassifier"
AUTHOR_EMAIL = "godthatback21@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)