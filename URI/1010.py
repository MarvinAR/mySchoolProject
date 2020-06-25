code1,product1,price1 = input().split()
code2,product2,price2 = input().split()
code1= int(code1)
product1 = int(product1)
price1 = float(price1)
code2 = int(code2)
product2 = int(product2)
price2 = float(price2)

VALORAPAGAR = price1*product1 + price2*product2
print("VALOR A PAGAR: R$ %.2f"%(VALORAPAGAR))