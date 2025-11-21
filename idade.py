def pode_entrar(idade):
    return idade >=18

def verificacao():
    print("Verificação de entrada. Digite 'sair' para encerrar.")

while True:

    nome = input ("\n Digite seu nome (ou 'sair' para encerrar): ").strip()
    if nome.lower() == "sair":
        print("Sistema encerrado. Até logo!")
        break

    try:
    
        idade = int(input("Qual a sua idade? "))
    except ValueError:
        print("Erro: A idade deve ser um número. Tente novamente.")
        continue
    if pode_entrar(idade):
        print(f"{nome}, Entrada permitida.")
    else:
        print(f"{nome}, Entrada não permitida.")

    verificacao()