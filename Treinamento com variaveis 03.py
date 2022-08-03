
a = 2
b = 0.5
c = 1
x = input("Digite o valor de x: ")

print(type(a))
print(type(b))
print(type(c))
print(type(x))

x = float(x) # aqui fazemos a conversão da string para o time numérico (Caso não tenha essa conversão, será retornado um erro de tipo)

y = a * x**2 + b * x + c
#y = 2 * 1**2 + 0,5 * 1 + 1
#y = 2 * 1 + 0,5 + 1
#y = 2 + 1,5
#y = 3,5

print(f" O resultado de y para x = {x} é {y}.")

print(type(a))
print(type(b))
print(type(c))
print(type(x))