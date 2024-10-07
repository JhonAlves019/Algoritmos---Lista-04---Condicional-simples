def autorizar_entrada():
    anuidade_em_dia = False
    valor_entrada = 25
    
    resposta = input("Você possui a anuidade em dia? (Sim/Não): ").strip().lower()
    
    if resposta == "sim":
        anuidade_em_dia = True
    
    if anuidade_em_dia:
        print("Entrada autorizada.")
    else:
        pagamento = input(f"Como sua anuidade não está em dia, você deve pagar {valor_entrada} reais pela entrada, gostaria de entrar, mesmo assim? (Sim/Não): ").strip().lower()
        
        if pagamento == "sim":
            print("Entrada autorizada.")
        else:
            print("Entrada negada.")

autorizar_entrada()
