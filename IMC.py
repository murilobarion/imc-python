print('Olá! Seja bem vindo ao Calculo de índice de Massa Corporal')

nome = input('Digite seu nome: ')

altura = float(input('Digite sua altura: '))

peso = float(input('Digite seu peso em KG: '))

imc = peso //  (altura * altura)

print(f'Nome: {nome}\nAltura: {altura}\nPeso: {peso}\n"Seu IMC: {imc}\n')