def main():
    produtos = [
        {"nome": "Tomate", "preço": 5.0},
        {"nome": "Cenoura", "preço": 3.0},
        {"nome": "Alface", "preço": 2.0},
        {"nome": "Batata", "preço": 4.0}
    ]

    total_compra = 0.0
    print("Bem-vindo à feira! Produtos disponíveis, no momento:")
    for produto in produtos:
        print(f"{produto['nome']} - R$ {produto['preço']} por kg")

    while True:
        produto_selecionado = input("Por favor, selecione um produto para comprar ou digite 'sair' para finalizar: ").strip()

        if produto_selecionado.lower() == 'sair':
            break

        # Buscar produto na lista
        produto_encontrado = next((p for p in produtos if p['nome'].lower() == produto_selecionado.lower()), None)

        if produto_encontrado:
            quantidade = float(input(f"Quantos quilos de {produto_selecionado} você deseja comprar? "))
            subtotal = quantidade * produto_encontrado['preço']
            total_compra += subtotal
            print(f"Você adicionou {quantidade} kg de {produto_selecionado} ao carrinho.")
        else:
            print("Produto não encontrado. Tente novamente.")
    print(f"O total da sua compra é: R$ {total_compra:.2f}")
    print("Pagamento deve ser à vista. Finalizando a compra...")
    print("Compra finalizada. Obrigado pela sua visita!")

if __name__ == "__main__":
    main()
