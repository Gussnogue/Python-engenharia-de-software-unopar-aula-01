
#ESTRUTURA CONDICIONAL SIMPLES:
ab = 5
abc = 10

if ab < abc :
    print("a é menor do que b")
    r = ab + abc
    print(r)

#ESTRUTURA COMPOSTA:

ba = 10
cba = 5

if ba < cba:
    print("ba é menor do que cba")
    ar = ba + cba
    print(ar)
else:
    print("ba é maior do que cba")
    ar = ba - cba
    print(r)

codigo_compra = 5111
if codigo_compra == 5222:
    print("Comprar à vista")
elif codigo_compra == 5333:
    print("Compra à prazo no boleto.")
elif codigo_compra == 5444:
    print("Compra à prazo no Cartão.")
else:
    print("Código não cadastrado")
    