from setuptools import setup, find_packages

VERSION = '1.0.1'
DESCRIPTION = 'A Simple 2D Vector Class'
LONG_DESCRIPTION = 'A Simple 2D Vector Class with standard functions used with vectors.'

setup(
        name="vector2d.py", 
        version=VERSION,
        author="Oxi-Dev0",
        author_email="x0floh@gmail.com",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        packages=find_packages(),
        install_requires=['math'],
        
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