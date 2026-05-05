
from setuptools import setup

setup(
    name="proxyfinder",
    version="1.0",
    py_modules=["proxy_finder_V1"], 
    install_requires=[
        "requests",
        "gevent",
        "urllib3"
    ],
    entry_points={
        "console_scripts": [
            "proxyfinder=proxy_finder_V2:main",
        ],
    },
)