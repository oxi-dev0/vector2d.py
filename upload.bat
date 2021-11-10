rmdir /s /q dist
python setup.py sdist bdist_wheel
twine upload dist/* --verbose