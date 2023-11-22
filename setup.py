import setuptools
with open("README.md","r",encoding="utf-8",) as f:
    long_description=f.read()
__version__="0.0.0"
REPO_NAME="NLP-MLOPS"
AUTHOR_USER_NAME="RAHULGUPTADATASCIENTIST"
SRC_REPO="Text_summarizer"
AUTHOR_EMAIL="rg48bbd@gmail.com"
setuptools.setup(name=SRC_REPO,
                 version=__version__,
                 author=AUTHOR_USER_NAME,
                 author_email=AUTHOR_EMAIL,
                 description="learning",
                 long_description="i am learning mlops",
                 url="https://github.com/RAHULGUPTADATASCIENTIST/NLP-MLOPS",
                 package_dir={" ":"src"},
                 packages=setuptools.find_packages(where="src"))