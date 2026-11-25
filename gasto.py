#05) Uma fábrica dará um abono salarial de R$ 200,00 aos seus empregados da seguinte forma: para
#os empregados com menos de cinco anos naquele emprego, receberão o abono os que tiverem salário de até R$ 1.400,00; já para aqueles com
#mais de cinco anos de casa, receberão os que tiverem salário de até R$ 1.500,00. Faça um algoritmo que
#leia, para um número desconhecido de empregados, o salário e o tempo no emprego, e informe se ele
#receberá ou não o abono. Ao final forneça as seguintes informações:
#a) número de empregados que possuem mais de cinco anos no emprego;
#b) o percentual de empregados que receberão o abono;
#c) o total a ser gasto pela empresa com o abono naquele mês;
#d) o total a ser gasto com os salários naquele mês. Obs: crie uma condição de parada para ser fornecida após os dados válidos.

empregados = int(input("Digite o numero de empregador: "))
abono = 200
contador=0
tempo = 0
recebe = 0
resto = 0
while empregados > 0 :
    salario = float(input("Digite o o salario do trabalhador: "))
    anos= float(input("Quantos anos este empregado trablhar aqui? "))

    if salario <= 1400 and anos < 5:
       
       print(" recebe abono")
       recebe+=1
    elif salario <= 1500 and anos > 5:

        print(" recebe abono")
        tempo+=1
    else:

        print("não recebe abono")
        resto = resto +  salario
       
    empregados-=1
    contador+=1
rece_abono = tempo+recebe
precentual = (recebe/contador)*100
gasto= abono*rece_abono
gasto_salarial=(1400*recebe)+(1500*tempo)+ resto

print("Numero de empregados que possuem mais de 5 anos: ", tempo)
print(f"O percentual de aempregados que consiguira abono:  {precentual}%")
print("Total de gasto pelo os abonos: "  ,gasto)
print("Total de gasto com salario mensal: ",gasto_salarial)


