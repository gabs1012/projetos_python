N = float(input("Digite quantas vezes dever ser somandas: "))



indicador =  0
contador = N
while contador > 0 :
    indicador= indicador + contador

    contador-=1

medio = indicador/N

print(f"a média dos números é: . {medio:.2f}".replace(".",","))