def processar_pedido():
    forma = input("Forma de pagamento: ").lower()
    valor = float(input("Valor: "))
    
    if forma == "cartão" and valor >= 20:
        print("Aceito!")
    elif forma == "pix" and valor > 0:  # PK provavelmente era PIX
        print("Aceito!")
    elif forma == "dinheiro" and valor == 10:  # Corrigido "CINHEIRO" para "dinheiro"
        print("Aceito!")
    else:
        print("Não aceito.")

print("=== Sistema de Pedidos da Lanchonete ===")
for i in range(3):
    print(f"\n--- Pedido {i + 1} ---")
    processar_pedido()

print("\n=== Fim dos pedidos ===")