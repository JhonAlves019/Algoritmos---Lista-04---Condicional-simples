def main():
    produtos = [
        {"nome": "Tomate", "preço": 5.0},
        {"nome": "Cenoura", "preço": 3.0},
        {"nome": "Alface", "preço": 2.0},
        {"nome": "Batata", "preço": 4.0}
    ]

    total_compra = 0.0
    carrinho = []
    print("Bem-vindo à feira! Produtos disponíveis, no momento:")
    for produto in produtos:
        print(f"{produto['nome']} - R$ {produto['preço']} por kg")

    anuidade_em_dia = input("Meu patrão/Minha patroa você está com a anuidade de associação de produtor rural em dia? (sim/não): ").strip().lower() == 'sim'

    if not anuidade_em_dia:
        print("Perdão, mas você não pode realizar a compra, pois não está com a anuidade em dia.")
        return

    valor_disponivel = float(input("Quanto dinheiro você tem disponível para a compra? R$ "))

    while True:
        produto_selecionado = input("Por favor, selecione um produto para comprar ou digite 'sair' para finalizar: ").strip()

        if produto_selecionado.lower() == 'sair':
            break

        produto_encontrado = next((p for p in produtos if p['nome'].lower() == produto_selecionado.lower()), None)

        if produto_encontrado:
            try:
                quantidade = float(input(f"Quantos quilos de {produto_selecionado} você deseja comprar? "))
                if quantidade <= 0:
                    print("Por favor, insira uma quantidade válida (maior que zero).")
                    continue
                subtotal = quantidade * produto_encontrado['preço']

                if total_compra + subtotal > valor_disponivel:
                    print("Você não tem dinheiro suficiente para essa compra, tente novamente.")
                    continue

                total_compra += subtotal
                carrinho.append({"nome": produto_selecionado, "quantidade": quantidade, "subtotal": subtotal})
                print(f"Você adicionou {quantidade} kg de {produto_selecionado} ao carrinho.")
            except ValueError:
                print("Entrada inválida. Por favor, insira um número válido.")
        else:
            print("Produto não encontrado. Tente novamente.")

    print("\nSeu carrinho de compras:")
    for item in carrinho:
        print(f"{item['quantidade']} kg de {item['nome']} - R$ {item['subtotal']:.2f}")

    print(f"\nO total da sua compra é: R$ {total_compra:.2f}")
    print("Pagamento deve ser à vista. Finalizando a compra, um momento...")
    print("Compra finalizada. Obrigado pela sua visita e volte sempre!")

if __name__ == "__main__":
    main()
