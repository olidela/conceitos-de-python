import time
from datetime import date
print('Insira seu dia de nascimento entre 1 e 30')
dia = int(input())

print('Insira seu mes de nascimento entre 1 e 12')
mes = int(input())

print('Insira seu ano de nascimento exemplo (1999)')
ano = int(input())

#Foram identificadas três possibilidades, o passado o presente e o futuro.

today = date.today() # define a data de hoje

idade = today.year - ano #define a idade do usuário baseado no ano atual.

if mes >= today.month: # caso o mês (input) seja maior ou igual que o mês atual:

    existencia_anos = idade - 1 #Como ainda não fez aniversário subtrai 1 de idade.
    print (existencia_anos, "anos")

else:

    print(idade, "anos") #Mas caso já tenha feito, apenas apresenta idade.

if today.month > mes: # se o mês atual for maior que o mês de nascimento:

    mes_existencia= today.month - 1 - mes # neste momento a função foi montada se baseando no fato
    #de uma pessoa já ter feito aniversário, permitindo que a contagem dos meses seja apenas até o aniversário.
    #a pergunta foi: como fazer um usuário apresentar 0 meses caso tenha passado dias do seu aniversário?
    #sendo assim me baseei na data 18-10-1996, o mês atual (11) - 1 apresenta o mẽs que ele nasceu, porém como eu
    #quero que a função retorne 0, subtrai com o mês declarado como input, mas lembre-se apenas quando o mẽs
    #atual é maior que o mês declarado.

    print (mes_existencia, "meses")

if today.month == mes and today.day < dia: #Quando o mês atual é igual de nascimento
    # e o dia atual é menor que o dia de nascimento
    print (today.month, "meses") #é permitido apresentar o mês atual pois até o dia do aniversário
    # não é completo um mẽs.

if today.month < mes: # mas se o mes atual for menor que o mês declarado como input.
    mes_existencia = today.month -1 #Essa parte eu coloquei pq quando eu colocava o mês 12, não aparecia
    #a contagem de meses, foi uma forma de resolver este problema.
    print(mes_existencia, "meses") # Na verdade acredito que essa parte existe pq eu precisava atender vários cenários.

if today.day == dia and today.month == mes and today.year == ano: #Essa parte é pra caso o nascimento for hoje
    print(0, "dias")
    print(0, "meses")

if dia == today.day: #Esta eu queria fazer se dia atual for diferente de dia(input), mas ai pycharm sugeriu assim
    pass
else:
    existencia_dias = 31 - dia + today.day #esta fórmula a princípio era pra ser 31 para os meses terminados em 31
    #e 30 para meses terminados em 30, porém se mostrou efetivo apenas com 31 menos o dia de nascimento mais o dia atual.
    print(existencia_dias, "dias")

















