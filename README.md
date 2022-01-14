<p align="center">
   <img src="https://github.com/oxi-dev0/vector2d.py/blob/main/Images/logo.png?raw=true" width=300>
</p>

<h1 align="center"> Vector2D.py </h2>
<p align="center">
    <a href="https://pypi.org/project/vector2d.py/">
        <img src="https://badgen.net/pypi/v/vector2d.py/">
    </a>
</p>
<p align="center">
    <a href="#">
        <img src="https://img.shields.io/github/repo-size/oxi-dev0/Vector2D.py" alt="Repo Size">
    </a>
    <a href="https://pypi.org/project/vector2d.py/">
        <img src="https://img.shields.io/github/downloads/oxi-dev0/vector2d.py/total" alt="Downloads">
    </a>
    <a href="#">
        <img src="https://img.shields.io/github/stars/oxi-dev0/vector2d.py" alt="Stars">
    </a>
    <a href="Look%20at%20this%20simple%20Vector2D%20Class%20for%20python%21%20https%3A%2F%2Fgithub.com%2Foxi-dev0%2Fvector2d.py">
      <img src="https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Foxi-dev0%2Fvector2d.py" alt="Tweet">
    </a>
</p>

<h3 align="center"> A small, but fast 2D Vector class for python 3.x</h3>
<br>
<h2> Installation </h2>

```
pip3 install vector2d.py
```

<h2> Usage </h2>

Import the Vector2D Class:
```python
from vector2d import Vector2D
```

<h2> Documentation </h2>

Creating a new vector:
```python
vector = Vector2D(x, y)
vector = Vector2D.UnitRandom()
vector = Vector2D.Zero()
vector = Vector2D.One()
```

<br>

Vectors support all basic operations with other Vectors, integers, or floats:
```python
a+b
a-b
a*b
a/b
a//b
```
<br>

Vectors support comparison with other Vectors:
```python
a==b
a!=b
a>b
a<b
a<=b
a>=b
```
<br>

You can access a Vector's length with the .length parameter:
```python
a.length
```
> :warning: **len(a) will not work**: It will throw an error!

<br>

You can normalise a Vector using .getNormalised():
```python
a.getNormalised()
```

<br>

You can project a Vector onto another using .Project():
```python
Vector2D.Project(a,b)
```
(Projects A onto B)

<br>

You can Linearly Interpolate between two points like this:
```python
Vector2D.Lerp(a,b,t)
```
`t` being the time value between a and b

<br>

You can get the distance between two points like this:
```python
Vector2D.Distance(a,b)
```

<br>

You can get the dot or cross product like this:
```python
Vector2D.DotProduct(a,b)
Vector2D.CrossProduct(a,b)
```

<br>

You can check if two segments are intersecting like this:
```python
Vector2D.isIntersecting(p1,p2,p3,p4)
```
With p1-4 representing points on two lines (p1-2: line 1, p3-4: line 2)
