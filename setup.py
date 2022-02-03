from setuptools import setup, find_packages

VERSION = '1.2.1'
DESCRIPTION = 'A small, but fast 2D Vector class for python 3.x'
LONG_DESCRIPTION = 'A small, but fast 2D Vector class for python 3.x, with standard Vector functions.'
URL = 'https://github.com/oxi-dev0/vector2d.py'

setup(
        name="vector2d.py", 
        version=VERSION,
        author="Oxi-Dev0",
        author_email="x0floh@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        py_modules=['vector2d'],
        install_requires=[],
        url=URL,
        
        project_urls={'Github': 'https://github.com/oxi-dev0/vector2d.py'},

        keywords=['python', 'vector', 'math'],
        classifiers= [
            "Development Status :: 5 - Production/Stable",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Natural Language :: English",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
            "Topic :: Utilities"
        ]
)