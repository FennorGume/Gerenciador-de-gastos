# Organizador de gastos em Python
import os

# Salario bruto do usuario e lista de gastos
while True:
    try:
        salario_bruto = float(input('Digite seu salario bruto ao mês: '))
        break
    except ValueError:
        os.system('cls')
        
gastos = []
categorias = {'1': 'moradia', '2': 'alimento', '3': 'assinaturas'}

# Bloco do calculo do INSS
def calc_inss(salario):
    if salario <= 1320.00:
        aliquota = 0.075 # 7,5%
    elif 1320.01 <= salario <= 2571.29:
        aliquota = 0.09 # 9%
    elif 2571.30 <= salario <= 3856.94:
        aliquota = 0.12 # 12#
    else: # salario >= 3856.95
        aliquota = 0.14 # 14%
    desconto = salario * aliquota
    return desconto

# Função para descontar valor dos gastos no salario apos INSS
def desconto_gastos(salario):
        if not gastos:
            return salario
        for valores in gastos:
            salario -= valores['valor']
        return salario

# Função para ver a lista de gastos
def vendo_gastos(escolhida):
    for gasto in gastos:
        if gasto['categoria'] == escolhida:
            print(f'Descrição: {gasto["descricao"]} Valor R${gasto["valor"]:.2f}')
    input('')

# Função para adicionar gastos
def adicionando_gastos(desc, val, categ):
    gastos.append({"descricao": desc, "valor": val, 'categoria': categ})

# Função para adicionar saldo extra
def saldo_extra(extra):
    valor_final = extra + salario_liquido
    return valor_final

# Descontando INSS e Gastos e adicionando saldo
desconto_inss = calc_inss(salario_bruto)
salario_liquido = salario_bruto - desconto_inss

# Loop do MENU
while True:
    os.system('cls')

    restante = desconto_gastos(salario_liquido)

    # Inicio
    print('Bem vindo.\n')
    if restante > 0:
        print(f'Seu salario apos descontos e gastos atuais é de \033[32mR${restante:.2f}\033[0m')
    elif restante <= 0:
        print(f'Seu salario apos descontos e gastos atuais é de \033[31mR${restante:.2f}\033[0m')

    menu = input('\n1. Adicionar gasto  \n2. Ver gastos \n3. Editar gastos \n4. Adicionar saldo \n\n"S". Para Sair\n').lower()
    if menu.startswith('s'):
        print('Saindo...')
        break

    add_gasto = menu.startswith('1')
    see_gasto = menu.startswith('2')
    edit_gasto = menu.startswith('3')
    add_saldo = menu.startswith('4')

    # Adicionando gastos
    if add_gasto:
        try:
            os.system('cls')
            choosing_categoria = input(f'Qual categoria gostaria de adicionar?\n \n1. Moradia \n2. Alimento \n3. Assinaturas \n')
            choosing_desc = input(f'Digite a descrição do seu gasto: ').capitalize()
            choosing_valor = float(input(f'Digite o valor mensal do seu gasto: '))

            nova_categoria = categorias[choosing_categoria]

            confirmacao = input('Pressione "S" para confirmar esta ação. ').lower()
            if confirmacao == "s":
                adicionando_gastos(choosing_desc, choosing_valor, nova_categoria)
                print('Gasto adicionado.')
            else:
                print('Nada foi adicionado, Retornando.')
            input('')
            
        except:
            print('Nada foi adicionado, Retornando.')

    # Vendo os gastos
    if see_gasto:
        os.system('cls')
        escolhendo_catregoria = input(f'Categorias:\n \n1. Moradia \n2. Alimento \n3. Assinaturas \n')
        try:
            os.system('cls')
            categoria = categorias[escolhendo_catregoria]
            vendo_gastos(categoria)

        except KeyError:
            print('Entrada invalida.')
            input('')
            
    # Editando os gastos
    if edit_gasto:
        os.system('cls')

    # Adicionando saldo extra
    if add_saldo:
        os.system('cls')
        print('Adicione saldo extra/ganhos adicionais.\n')
        qnt_adicionar = float(input(f'Quando gostaria de adicionar? '))
        saldo_extra(qnt_adicionar)
        print(f'Saldo extra adicionado com exito. \033[32m+R${qnt_adicionar:.2f}\033[0m ')
        input('')