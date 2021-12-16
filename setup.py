import setuptools
from subprocess import check_call
import os.path as osp
from pathlib import Path

install_requires = \
    [
        'pycocotools ;platform_system!="Windows"',
        'pycocotools-windows ;platform_system=="Windows"',
        'chardet',
        'imantics',
        'pandas',
        'openpyxl',
    ]

root = Path(__file__).parent
check_call("conda install -y --file".split()+[str(root/"requirements.txt")])
setuptools.setup(
    name="MLObject",
    version="1.0.0",
    author="zmfkzj",
    author_email="qlwlal@naver.com",
    description="ML object",
    packages=setuptools.find_packages(),
    install_requires=install_requires,
)
