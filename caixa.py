# Simulador de Caixa (mercado simples)

# Cadastro do cliente
nome = input("Digite o nome do cliente: ")
resposta_cpf = input("Deseja digitar o CPF? (s/n): ").lower()
if resposta_cpf =='s':
    CPF = input("Digite o CPF: ")
else:
    CPF = print(f"CPF não informado")
saldo = float(input("Digite o saldo do cliente: "))

# Itens disponíveis
itens = {
    1: ("Arroz", 15.50),
    2: ("Feijão", 12.30),
    3: ("Macarrão", 8.90),
    4: ("Rosquinha Mabel", 6.90)
}

movimentacoes = [] # lista para registrar movimentações
total_compras = [] # lista para registrar total de compras
total_compras = sum(total_compras)
def extrato(saldo_final):
    print(f"Total de compras: R$ {total_compras}")
    print(f"Total final: R$ {total_compras}")    
    print("\n======= RECIBO DE COMPRAS =======")    
    print(f"Cliente: {nome} | Saldo: R$ {saldo:.2f}\n")

    if not movimentacoes:
        print("Nenhuma compra realizada.")
    else:
        '''total_compras = [] # lista para registrar total de compras
        total_compras.append(total) # adiciona o total da compra na lista
        total_compras = sum(total_compras)'''
        for m in movimentacoes:
            print(m)
    print(f"\nTotal final: R$ {total_compras:.2f}\n")
    print(f'Saldo restante: R$ {saldo:.2f}')
    print("Obrigado e volte sempre!!!")
    print("=================================")

print(f"\nBem-vindo, {nome}! Seu saldo inicial é R$ {saldo:.2f}\n")


def adicionar_produto():
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    itens[len(itens) + 1] = (produto, preco)
    print("Produto adicionado com sucesso!")
# Loop de compras
while True:
    print("\n--- Lista de Opções ---")
    for codigo, (produto, preco) in itens.items(): #
        print(f"{codigo} - {produto} - R$ {preco:.2f}")
    
    print("0 - Finalizar compras e imprimir recibo")

    escolha = int (input("\nEscolha a opção: "))
    
    if escolha == 99 :
        adicionar_produto()
        continue    

    if escolha == 0:
        extrato(total_compras)  # Mostra recibo final
        break

    elif escolha in itens:
        produto, preco = itens[escolha] # 
        quantidade = int(input(f"Quantas unidades de {produto} você deseja comprar? "))
        total = preco * quantidade  
        print(f"Total: R$ {total:.2f}") 
                
        if saldo >= total: # verifica se o saldo é suficiente
            saldo -= total
            movimentacoes.append(f"{quantidade} - {produto} - R$ {preco:.2f} = {total:.2f}") # adiciona a movimentação na lista
            total_compras = total_compras + total # adiciona o total da compra na lista
            print(f"\n{nome} comprou, {quantidade} {produto} por R$ {preco:.2f} x {quantidade} = {total:.2f}")
            print(f'Total: {total_compras:.2f}') 
            
        else:
            print(f"\nSaldo insuficiente para comprar.")
    else:
        print("\nOpção inválida! Tente novamente.")
        
        