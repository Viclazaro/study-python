# Desenvolva um gerador de tabuada, capaz de gerar a tabuada
# de qualquer número inteiro entre 1 a 10. O usuário deve informar de qual numero
# ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:

x = int(input('Tabuada do numero: '))
for i in range(0, 11):
    conta = x * i
    print(f'{x} x {i} = {conta}')