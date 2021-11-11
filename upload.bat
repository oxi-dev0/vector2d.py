rmdir /s /q dist
rmdir /s /q build
rmdir /s /q vector2d.py.egg-info
python setup.py sdist bdist_wheel
twine upload dist/* --verbose