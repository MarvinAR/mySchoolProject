A,B,C = input().split()
A = float(A)
B = float(B)
C = float(C)
tri = (A * C)/2
circle = 3.14159*C*C
trape = ((A+B)*C)/2
square = B*B
rectang = A*B
print("TRIANGULO: %.3f"%(tri))
print("CIRCULO: %.3f"%(circle))
print("TRAPEZIO: %.3f"%(trape))
print("QUADRADO: %.3f"%(square))
print("RETANGULO: %.3f"%(rectang))