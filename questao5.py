usuario = str(input("Por favor, informe seu nome:"))
senha = str(input("Por favor, digite aqui a senha que criou:"))
confirme_senha = str(input("Por favor, repita a senha escolhida, anteriormente:"))
if senha == confirme_senha:
    print("Seu cadastro foi validado, seja bem-vindo,", usuario)
else:
    print ("Falha no cadastro, as senhas não conferem. Por favor, tente novamente")
