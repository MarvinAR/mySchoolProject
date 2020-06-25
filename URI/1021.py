N = float(input())
N = int(N*100)
print("NOTAS:")
A = N//10000#int(N/100)
N -= 10000*A
print("%i nota(s) de R$ 100.00" % (A))

A = N//5000
N -= 5000*A
print("%i nota(s) de R$ 50.00" % (A))

A = N//2000
N -= 2000*A
print("%i nota(s) de R$ 20.00" % (A))

A = N//1000
N -= 1000*A
print("%i nota(s) de R$ 10.00" % (A))

A = N//500
N -= 500*A
print("%i nota(s) de R$ 5.00" % (A))

A = N//200
N -= 200*A
print("%i nota(s) de R$ 2.00" % (A))
print("MOEDAS:")
A = N//100
N -= 100*A
print("%i moeda(s) de R$ 1.00" % (A))

A = N//50
N -= 50*A
print("%i moeda(s) de R$ 0.50" % (A))

A = N//25
N -= 25*A
print("%i moeda(s) de R$ 0.25" % (A))

A = N//10
N -= 10*A
print("%i moeda(s) de R$ 0.10" % (A))

A = N//5
N -= 5*A
print("%i moeda(s) de R$ 0.05" % (A))

A = N//1
N -= 1*A
print("%i moeda(s) de R$ 0.01" % (A))