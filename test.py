from vector2d import Vector2D
import time

def getms():
    return round(time.time()*1000)

a = Vector2D.UnitRandom() #Vector2D(0, 5)
b = Vector2D(5, 10)
c = Vector2D(2, 3)

print("Validity Checks:")

print("A: " + str(a))
print("B: " + str(b))
print("C: " + str(c))

print("A + B: " + str(a+b))
print("A - B: " + str(a-b))
print("A * B: " + str(a*b))
print("A / B: " + str(a/b))
print("A // B: " + str(a//b))

print(f"10 / b (rdiv): {10/b}")
print(f"15 % c (rmod): {2%c}")

print("Length A: " + str(a.length))
print("Length B: " + str(b.length))

print("Normalised B: " + str(b.getNormalised()))

print("A dot B: " + str(Vector2D.DotProduct(a,b)))
print("A cross B: " + str(Vector2D.CrossProduct(a,b)))

lerp = Vector2D.Lerp(a, b, 0.65)
print("0.65 Lerp A B: " + str(lerp))
print(f"Inverse Lerp A, B, {lerp}: {Vector2D.InverseLerp(a, b, lerp)}")

print("Norm A dot Norm B: " + str(Vector2D.DotProduct(a.getNormalised(), b.getNormalised())))

print("A == B? " + str(a == b))
print("A == A? " + str(a == a))

print("Random unit: " + str(Vector2D.UnitRandom()))

print("Zero: " + str(Vector2D.Zero()))
print("One: " + str(Vector2D.One()))

print("Distance A, B: " + str(Vector2D.Distance(a,b)))
print(f"B - A Length: {(b-a).length}")