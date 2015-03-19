from random import randint
n1=0
n2=0

while (n1<3) and (n2<3):
    player1=input("Pedra, papel, tesoura, lagarto ou spock? (Quem fizer 3 pontos seguidos ganha)")
    computador=randint(1,5)
    if (computador==1):
        computador="pedra"
    elif (computador==2):
        computador="papel"
    elif (computador==3):
        computador="tesoura"
    elif (computador==4):
        computador="lagarto"
    else:
        computador="spock"
    if (player1=="pedra" and computador=="tesoura"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="pedra" and computador=="lagarto"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="tesoura" and computador=="papel"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="tesoura" and computador=="lagarto"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="papel" and computador=="pedra"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="papel" and computador=="spock"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="lagarto" and computador=="spock"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="lagarto" and computador=="papel"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="spock" and computador=="pedra"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="spock" and computador=="tesoura"):
        print("Ponto para o Player1")
        n1=n1+1
        n2=0
    elif (player1=="lagarto" and computador=="pedra"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="tesoura" and computador=="pedra"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1        
    elif (player1=="pedra" and computador=="papel"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1    
    elif (player1=="spock" and computador=="papel"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="papel" and computador=="tesoura"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="lagarto" and computador=="tesoura"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="pedra" and computador=="spock"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="tesoura" and computador=="spock"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="papel" and computador=="lagarto"):
        print("Ponto para o  computador")
        n1=0
        n2=n2+1
    elif (player1=="spock" and computador=="lagarto"):
        print("Ponto para o computador")
        n1=0
        n2=n2+1
    elif (player1=="pedra" and computador=="pedra"):
        print("Empatou")
        n1=0
        n2=0
    elif (player1=="papel" and computador=="papel"):
        print("Empatou")
        n1=0
        n2=0
    elif (player1=="tesoura" and computador=="tesoura"):
        print("Empatou")
        n1=0
        n2=0
    elif (player1=="lagarto" and computador=="lagarto"):
        print("Empatou")
        n1=0
        n2=0
    elif (player1=="spock" and computador=="spock"):
        print("Empatou")
        n1=0
        n2=0
    if (n1==3):
        print("Parabéns voce venceu!")
    if (n2==3):
        print("Mais sorte da próxima vez.")
