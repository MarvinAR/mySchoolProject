N = int(input())
print(N)
A = N//100#int(N/100)
N -= 100*A
print("%i nota(s) de R$ 100,00" % (A))

A = N//50
N -= 50*A
print("%i nota(s) de R$ 50,00" % (A))

A = N//20
N -= 20*A
print("%i nota(s) de R$ 20,00" % (A))

A = N//10
N -= 10*A
print("%i nota(s) de R$ 10,00" % (A))

A = N//5
N -= 5*A
print("%i nota(s) de R$ 5,00" % (A))

A = N//2
N -= 2*A
print("%i nota(s) de R$ 2,00" % (A))

A = N//1
N -= 1*A
print("%i nota(s) de R$ 1,00" % (A))