def verificar_cotista():
    bolsa_familia = input("Você possui bolsa família? (S para sim/N para não): ").strip().upper()
    mais_de_tres_filhos = input("Você possui mais de três filhos? (S para sim/N para não): ").strip().upper()
    
    if bolsa_familia == 'S' and mais_de_tres_filhos == 'S':
        return True
    else:
        return False

resultado = verificar_cotista()
if resultado:
    print("Verdadeiro: Você pode acessar à vaga de cotista, parabéns.")
else:
    print("Falso: Você não pode acessar à vaga de cotista, providencie mais filhos.")
