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

Definitions
```python
vector = Vector2D(x, y)
vector = Vector2D.UnitRandom()
vector = Vector2D.Zero()
vector = Vector2D.One()
```

<br>

Operations
```python
a+b
a-b
a*b
a/b
a//b
```
> **Vectors support operations with other Vectors, integers, or floats.**

<br>

Comparison
```python
a==b
a!=b
a>b
a<b
a<=b
a>=b
```
<br>
<br>

Length
```python
a.length
# or
len(a)
```
<br>

Normalise
```python
a.getNormalised()
```

<br>
<br>

Vector Projection
```python
Vector2D.Project(a,b)
```
(Projects A onto B)

<br>
<br>

Linear Interpolation
```python
Vector2D.Lerp(a,b,t)
```
`t` being the time value between a and b

<br>

Inverse Linear Interpolation
```python
Vector2D.InverseLerp(a,b,v)
# Returns t
```
`t` being the time value between a and b
and `v` being the vector between a and b

<br>
<br>

Distance Calculation
```python
Vector2D.Distance(a,b)
```

<br>
<br>

Dot and Cross Products
```python
Vector2D.DotProduct(a,b)
Vector2D.CrossProduct(a,b)
```

<br>
<br>

Calculating an intersection between two line segments
```python
Vector2D.Intersection(p1, p2, p3, p4)
```
(P1-2: Line 1, P3-4: Line 2)
