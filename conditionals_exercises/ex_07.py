# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.

# Desconto do IR:
# Salário Bruto até 900 (inclusive) - isento
# Salário Bruto até 1500 (inclusive) - desconto de 5%
# Salário Bruto até 2500 (inclusive) - desconto de 10%
# Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.

#    Salário Bruto: (5 * 220)        : R$ 1100,00
#    (-) IR (5%)                     : R$   55,00 
#    (-) INSS ( 10%)                 : R$  110,00
#   FGTS (11%)                       : R$  121,00
#    Total de descontos              : R$  165,00
#    Salário Liquido                 : R$  935,00

valor_hora = float(input('Informe o valor da sua hora: '))
horas_trabalhadas = float(input('Informe a quantidade de horas trabalhadas no mês: '))


salario_bruto = valor_hora * horas_trabalhadas

if salario_bruto <= 900:
    ir_percentual = 0  
elif salario_bruto <= 1500:
    ir_percentual = 5
elif salario_bruto <= 2500:
    ir_percentual = 10
else:
    ir_percentual = 20

ir = (ir_percentual / 100) * salario_bruto
inss = (10 / 100) * salario_bruto
sindicato = (3 / 100) * salario_bruto
fgts = (11 / 100) * salario_bruto  
total_descontos = ir + inss + sindicato
salario_liquido = salario_bruto - total_descontos

print(f'''
Salário Bruto: ({valor_hora:.2f} * {horas_trabalhadas:.0f})        : R$ {salario_bruto:.2f}
(-) IR ({ir_percentual}%)                     : R$ {ir:.2f}
(-) INSS (10%)                  : R$ {inss:.2f}
(-) Sindicato (3%)              : R$ {sindicato:.2f}
FGTS (11%)                      : R$ {fgts:.2f}
Total de descontos              : R$ {total_descontos:.2f}
Salário Líquido                 : R$ {salario_liquido:.2f}
''')
