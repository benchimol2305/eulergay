#Juego de blackjack
import random
import time
#indicamos las variables
i=0
a=0
b=0
t=0
balance=700
while i==0:
    #bet
    while a==0:
        print(f"tu balance actual es: {balance}")
        time.sleep(1)
        bet=int(input("Dime cual es la cantidad que deseas apostar"))
        if balance>=bet and bet>0:
            balance-=bet
            a=1
        elif balance<bet:
            print("la cantidad que quieres apostar supera tu saldo actual")
            time.sleep(1)
        elif bet<0:
            print("la cantidad es negativa, no se puede apostar")
            time.sleep(1)
    time.sleep(1)
    a=0
    #se agregan las cartas 
    cards=[2,3,4,5,6,7,8,9,10,10,10,10,11]
    hcards=[1,2,3,4,5,6,7,8,9,10,10,10,10,11]
    rand1= random.randint(0,12)
    rand2= random.randint(0,12)
    primera_carta=cards[rand1]
    segunda_carta=cards[rand2]
    total=primera_carta+segunda_carta
    print("revolviendo las cartas")
    time.sleep(2)
    print(f"obtienes un ")
    time.sleep(1)
    print(f"{primera_carta}")
    time.sleep(1)
    print("y")
    time.sleep(1)
    print(f"{segunda_carta}")
    time.sleep(1)
    if not primera_carta==11 and not segunda_carta==11:
       total=primera_carta+segunda_carta
       print(f"tu total es {total}")
    if primera_carta==11:
       total1=1+segunda_carta
       total2=11+segunda_carta
       print(f"tu total puede ser {total1} o {total2} ")
    if segunda_carta==11:
        total1= primera_carta+1
        total2=primera_carta+11
        print(f"tu total puede ser {total1} o {total2} ")
    all_cards= []
    time.sleep(1)
    rand_house1=random.randint(0, 13) 
    house_cards1=hcards[rand_house1]   
    print(f"la casa recibe un {house_cards1}")
    time.sleep(1)

    while b==0:
        otra_carta= int(input("escribe 1 si quieres otra carta y 0 si te quieres quedar"))
        if otra_carta==1:
            randanotherone=random.randint(0, 12)
            the_otherone= cards[randanotherone]
            print(f"obtienes un {the_otherone}")
            time.sleep(1)
            if the_otherone==11:
                print("obtienes una As, que valor quieres obtener? 1 o 11")
                valor_as=int(input(": "))
                if valor_as==1:
                    the_otherone=1
                else:
                    the_otherone=11
            all_cards.append(the_otherone)
        time.sleep(1)                
        if otra_carta==0:
            b=1
    b=0     
    if primera_carta==11:
        print("Obtienes una as en tu primera carta, que valor quieres que sea? 1 o 11")
        valor_as=int(input(": "))
        if valor_as==1:
            primera_carta=1
        else:
            primera_carta=11
    if segunda_carta== 11:
        print("Obtienes una as en tu segunda carta, que valor quieres que sea? 1 o 11")       
        valor_as=int(input(": "))
        if valor_as==1:
            segunda_carta=1
        else:
            segunda_carta=11
    all_cards.append(primera_carta)
    all_cards.append(segunda_carta)
    time.sleep(1)
    totalex=sum(all_cards)
    time.sleep(1)
    print(f"estas son tus cartas {all_cards}")
    time.sleep(1)
    print(f"tu total final es {totalex}")
    time.sleep(2)
    print("Ahora le toca jugar a la casa")
    time.sleep (1)
    print(f"La primera carta de la casa fue {house_cards1}")
    rand_house2=random.randint(0, 13)
    house_cards2= cards[rand_house2]
    time.sleep(1)
    print(f"La casa recibe un {house_cards2}")
    all_cardshouse=[]
    all_cardshouse.append(house_cards1)
    all_cardshouse.append(house_cards2)
    total_de_la_casa=house_cards1+house_cards2
    time.sleep(1)

    while total_de_la_casa<=16:
        rand_anotherhouse= random.randint(0, 12)
        another_house=cards[rand_anotherhouse]
        all_cardshouse.append(another_house)
        total_de_la_casa +=another_house
        print(f"La casa solicita y obtiene {another_house}")
        time.sleep(1)
    totalex_house=sum(all_cardshouse)   
    time.sleep(2)
    print(f"tu resultado es {totalex} y el de la casa es {totalex_house}")
    time.sleep(2)
    if (totalex>21 and totalex_house>21) or (totalex== totalex_house and not totalex>21 and totalex_house>21):
      win=bet
      balance+= win
      print("empate, nadie gana")
    elif totalex<=totalex_house<=21:
       print("Perdiste")
    elif totalex==totalex_house:
        win=bet
        balance+=win
        print(f"hubo un empate obtienes {win}")   
    elif totalex_house<totalex<=21:
        win= bet*2
        balance+=win
        print(f"tu ganas {win}")
    elif totalex <=21 < totalex_house:
        win=bet*2
        balance+=win
        print(f"tu ganas {win}")
    else:
        print("Tu pierdes")   