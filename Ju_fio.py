import os
from prettytable import PrettyTable

print('+__________JU-Fio-de-Malha__________+\n')
table = PrettyTable(['Produto', 'Preço'])
total = 0

while True:
    name = input('Digite o Produto (ou digite \'fim\' para sair):')

    if name.lower() != 'fim':
        price = int(input('Digite o Preço:'))
        total += price
        table.add_row([name, price])
        continue

    elif name.lower() == 'fim':
        break

table.add_row(['TOTAL', total])

output_folder = 'Comprovantes'
os.makedirs(output_folder, exist_ok=True)

output_file_path = os.path.join(output_folder, 'Recibo.txt')
with open(output_file_path, 'w') as file:
    file.write(str(table) + '\n')
    file.write('\nObrigado pela Preferência! Volte sempre! :)\n')
    file.write(f'Seu total de compras foi {total}/-')

print(f'Seu total de compras foi {total}/-')
print(f'Os detalhes da fatura foram salvos em {output_file_path}')