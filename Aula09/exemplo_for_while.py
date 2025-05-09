# explicando for while

lst_vl = []

for i in range(5):
    num = int(input("informe o número: "))
    lst_vl.append(num)

print(f'Os Números são {lst_vl}')


# While
lst_nomes = []
resposta = ''

while resposta != 'n':
    nome = input('Informe o nome: ')
    lst_nomes.append(nome)
    resposta = input('Quer continuar? [s/n]: ')

print(f'os nome é {lst_nomes}')

lst_nomes2 = []
while True:
    nome = input('Informe o nome: ')
    lst_nomes2.append(nome)

    resposta = input('Quer continuar? ')
    if resposta == 'n':
        break
    print(nome)
