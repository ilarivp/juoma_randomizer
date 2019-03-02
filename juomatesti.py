import numpy as np
import os
import textwrap
import cmd
import sys
import time

screen_width = 100

class juomari:
    def __init__(self):
        self.name = ''
        self.juomat = 0
        self.vedet = 0
        self.juomat_putkeen = 0
        self.juomalista = []

juomarit = []

def startscreen():
    os.system('cls')
    print("#############################")
    print("#  JUOMAGENERAATTORI 666    #")
    print("#############################")
    print("# Syötä pelaajien lukumäärä #")
    lkm = 0
    while lkm == 0 or lkm > 10:
        lkm = input(">  ")
        lkm = lkm_to_int(lkm)
        if lkm > 10:
            print('Maksimipelaajamäärä on 10.') 
    for i in range(lkm):
        lisajuomari(True)
    title_screen()

def lkm_to_int(lkm):
    try:
        lkm = int(lkm)
    except:
        print("Yritä vähän kovempaa.")
        lkm = 0
    return(lkm)

def lisajuomari(startteri = False):
    juomari_temp = juomari()
    if startteri==False:
        print('Juomarit: ')
        for i in range(len(juomarit)):
            print(juomarit[i].name)
        print("")
    nimi = input('Anna juomarin nimi: ').lower()
    namelist = []
    for doku in juomarit:
        namelist.append(doku.name.lower())
    while nimi in namelist:
        print('Nimi', nimi, 'on jo käytössä.')
        nimi = input('Anna juomarin nimi: ').lower()
    juomari_temp.name = nimi
    lisajuoma = 'y'
    juomat = []
    while lisajuoma == 'y':
        juoma = input("Lisää juoma: ").lower()
        juomat.append(juoma)
        lisajuoma = input("Lisätäänkö toinen juoma? [y/n]: ")
        while lisajuoma not in ['y', 'n']:
            lisajuoma = input("Lisätäänkö toinen juoma? [y/n]: ")
    if 'vesi' in juomat:
        juomat.remove('vesi')
    juomat.append('vesi')
    juomari_temp.juomalista = juomat
    juomarit.append(juomari_temp)
    if startteri==False:
        add_remove_menu()

def poista_seppo():
    player = ""
    print('Juomarit: ')
    for i in range(len(juomarit)):
        print(juomarit[i].name)
    print("")
    nimi = input("KUKA SIIN NETIS ON?!?!?: ")
    for i in range(len(juomarit)):
        if juomarit[i].name.lower() == nimi.lower():
            player=juomarit[i]
    if player == "":
        print('Player', nimi, 'not found.')
        input('Press <Enter> to continue')
        title_screen()
    else: 
        juomarit.remove(player)
        print('Player', nimi, 'removed.')
        input('Press <Enter> to continue')
        add_remove_menu()     

def poista_juoma():
    player = ""
    print('Juomarit: ')
    for i in range(len(juomarit)):
        print(juomarit[i].name)
    print("")
    while player == "":
        nimi = input("KUKA SIIN NETIS ON?!?!?: ")
        for i in range(len(juomarit)):
            if juomarit[i].name.lower() == nimi.lower():
                player=juomarit[i]
    print('')
    print('Juomat: ')
    for juoma in player.juomalista:
        print(juoma)
    print('')
    poistettava = input("Mikä juoma poistetaan? ")
    while poistettava == 'vesi':
        print('Ei voi poistaa juomaa "vesi".')
        poistettava = input("Mikä juoma poistetaan? ")
    try:
        player.juomalista.remove(poistettava)
        print('Juoma', poistettava, 'poistettu.')
        input('Press <Enter> to continue')
    except:
        print('Juomaa', poistettava, 'ei löydetty.')
        input('Press <Enter> to continue')
    add_remove_menu()

def lisaa_juoma():
    player = ""
    print('Juomarit: ')
    for i in range(len(juomarit)):
        print(juomarit[i].name)
    print("")
    while player == "":
        nimi = input("KUKA SIIN NETIS ON?!?!?: ")
        for i in range(len(juomarit)):
            if juomarit[i].name.lower() == nimi.lower():
                player=juomarit[i]
    print('')
    print('Juomat: ')
    for juoma in player.juomalista:
        print(juoma)
    print("")
    lisattava = input("Mikä juoma lisätään? ").lower()
    while lisattava in player.juomalista:
        print('Juoma', lisattava, 'on jo listalla.')
        print("")
        lisattava = input("Mikä juoma lisätään? ")
    player.juomalista.insert(len(player.juomalista)-1, lisattava)
    print('Juoma', lisattava, 'lisätään.')
    input('Press <Enter> to continue')
    add_remove_menu()


def juomageneraattori():

    numero = np.random.uniform()
    player = ""
    while player == "":
        print('Juomarit: ')
        for i in range(len(juomarit)):
            print(juomarit[i].name)
        print("")
        nimi = input('Kerro minulle nimesi ;)): ')
        for i in range(len(juomarit)):
            if juomarit[i].name == nimi:
                player=juomarit[i]
        if player == "":
            print('Player', nimi, 'not found.')
            input('Press <Enter> to continue')
            title_screen()
    
    numero = int(np.floor(numero*(len(player.juomalista)+player.juomat_putkeen)))
    vesi_index = len(player.juomalista)-1
    if numero > (vesi_index): 
        numero = vesi_index
    juoma = player.juomalista[numero]
    player.juomat_putkeen += 1
    if numero == (vesi_index):
        player.juomat_putkeen = 0
        player.vedet += 1
        print('Hähää, juo', juoma)
    else:
        player.juomat += 1
        print('SOOSIIII, juo', juoma)
    input('Press <Enter> to continue')
    title_screen()


def title_screen_selections():
    option = input("> ")
    if option.lower() in ["juomalista", "1"]:
        show_drinks()  
    elif option.lower() == ("pelaa") or option.lower() == "2":
        juomageneraattori() 
    elif option.lower() == ("tilanne") or option.lower() == "3":
        show_status()
    elif option.lower() == ("muokkaa") or option.lower() == "4":
        add_remove_menu()
    elif option.lower() == ("quit") or option.lower() == "0":
        sys.exit()
    while option.lower() not in ["juomalista", "pelaa", "muokkaa", "quit", "1", "2", "3", "4", "0"]:
        print('Yritä vähän enempi')
        option = input("> ")
        if option.lower() == ("juomalista") or option.lower() == "1":
            show_drinks()  
        elif option.lower() == ("pelaa") or option.lower() == "2":
            juomageneraattori()
        elif option.lower() == ("tilanne") or option.lower() == "3":
            show_status()
        elif option.lower() == ("muokkaa") or option.lower() == "4":
            add_remove_menu()
        elif option.lower() == ("quit") or option.lower() == "0":
            sys.exit()

def add_remove_menu_selections():
    option = input("> ")
    if option.lower() == ("uusi juomari") or option.lower() == "1":
        lisajuomari()
    elif option.lower() == ("poista juomari") or option.lower() == "2":
        poista_seppo()
    elif option.lower() == ("poista juoma") or option.lower() == "3":
        poista_juoma()
    elif option.lower() == ("lisää juoma") or option.lower() == "4":
        lisaa_juoma()
    elif option.lower() == ("return") or option.lower() == "0":
        title_screen()
    while option.lower() not in ["uusi juomari", "poista juomari", "poista juoma", "lisää juoma", "return", "1", "2", "3", "4", "0"]:
        print('Yritä vähän enempi')
        option = input("> ")
        if option.lower() == ("uusi juomari") or option.lower() == "1":
            lisajuomari()
        elif option.lower() == ("poista juomari") or option.lower() == "2":
            poista_seppo()
        elif option.lower() == ("poista juoma") or option.lower() == "3":
            poista_juoma()
        elif option.lower() == ("lisää juoma") or option.lower() == "4":
            lisaa_juoma()
        elif option.lower() == ("return") or option.lower() == "0":
            title_screen()


def title_screen():
    os.system('cls')
    print("############################")
    print("#  JUOMAGENERAATTORI 666   #")
    print("# 1. Juomalista            #")
    print("# 2. Pelaa                 #")
    print("# 3. Tilanne               #")
    print("# 4. Muokkaa juomia/juojia #")    
    print("# 0. Quit                  #")
    print("############################")
    title_screen_selections()

def add_remove_menu():
    os.system('cls')
    print("###########################")
    print("#  JUOMAGENERAATTORI 666  #")
    print("# 1. Uusi juomari         #")    
    print("# 2. Poista juomari       #")    
    print("# 3. Poista juoma         #")    
    print("# 4. Lisää juoma          #")    
    print("# 0. Return               #")
    print("###########################")
    add_remove_menu_selections()

def show_drinks():
    os.system('cls')
    print("#########################")
    print("# JUOMAGENERAATTORI 666 #")
    print("#########################")
    print("# Juomalistat:           ")
    for player in juomarit:
        print("# ", player.name)
        print("# ", player.juomalista)
        print("#                         ")
    print("# 0. Return                ")
    print("#########################")
    option = input("> ")
    if option.lower() == ("return") or option.lower() == "0":
        title_screen()
    while option.lower() not in ["return", "0"]:
        print('Väärä valinta')
        option = input("> ")
        if option.lower() == ("return") or option.lower() == "0":
            title_screen()

def show_status():
    os.system('cls')
    print("#########################")
    print("# JUOMAGENERAATTORI 666 #")
    print("# Tilanne:               ")
    print("#                         ")
    for player in juomarit:
        print("# #", player.name, "#")
        print("# alkoholit: ", player.juomat)
        print("# vedet:     ", player.vedet)
        print("#                         ")
    print("# 0. Return                ")
    print("#########################")
    option = input("> ")
    if option.lower() == ("return") or option.lower() == "0":
        title_screen()
    while option.lower() not in ["return", "0"]:
        print('Väärä valinta')
        option = input("> ")
        if option.lower() == ("return") or option.lower() == "0":
            title_screen()

startscreen()  # initiates screen

# TODO(): Juomalistan juomien printtaus allekkain 