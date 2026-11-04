compras = int(input(" Quantos itens deseja adicionar ? "))

nomes = []

for c in range(compras):
    nomeProduto = input('Digite o nome do produto : ')
    nomes.append(nomeProduto)

print('=' * 40 )
for nome in nomes:
    print(f'a lista completo ficou {nome}')

remover = input('Deseja remover algum item ? ')

if remover == 's':
    remover = input('Digite o nome do produto que deseja remover : ')
    nomes.remove(remover)

for final in nomes:
    print(f'a lista final ficou {final}')
