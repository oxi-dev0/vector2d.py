from vector2d import Vector2D
import time

def getms():
    return round(time.time()*1000)

a = Vector2D(0, 5)
b = Vector2D(5, 10)

print("Validity Checks:")

print("A: " + str(a))
print("B: " + str(b))

print("A + B: " + str(a+b))
print("A - B: " + str(a-b))
print("A * B: " + str(a*b))
print("A / B: " + str(a/b))
print("A // B: " + str(a//b))

print("Length A: " + str(a.length))
print("Length B: " + str(b.length))

print("Normalised B: " + str(b.getNormalised()))

print("A dot B: " + str(Vector2D.DotProduct(a,b)))
print("A cross B: " + str(Vector2D.CrossProduct(a,b)))

print("Norm A dot Norm B: " + str(Vector2D.DotProduct(a.getNormalised(), b.getNormalised())))

print("A == B? " + str(a == b))
print("A == A? " + str(a == a))

print("Random unit: " + str(Vector2D.UnitRandom()))

print("Zero: " + str(Vector2D.Zero()))
print("One: " + str(Vector2D.One()))

print("Error Test")
c = a + "hi"
