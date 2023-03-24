# fazer um programa que lia o nome do usuario, e que em seguida informe o nome dele no print ex: Olá, nome do usuario....
# No input pedir que seja informado o que ele deseja
def Nome_User():
    nome = input("Olá, por favor informe seu nome: ")
    # Caso as abrir uma chave para escolha de opções, para inserir o valor de uma das cadeias
    DelT = float(input("Qual o tempo? "))
    DelV = float(input("Qual a duração? "))
    #calculo para acharmos o deslocamento, Vm = DeltaS/DeltaT
    Vm = (DelT / DelV)
    # informa a velocidade média
    print("Olá, {} resultado do calculo é {:.2f}".format(nome, Vm))

Nome_User()