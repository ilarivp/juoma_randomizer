import numpy as np
import os
import textwrap
import sys
import juomarit as kulli

def lisaa_pelaaja(juomarit, uusi_juomari):
#    for nimi in juomarit:
#        if nimi.name.lower() == uusi_juomari.lower():
#            break
    new_juomari = kulli.Juomari()
    new_juomari.name = uusi_juomari.lower()
    juomarit.append(new_juomari)
    return(juomarit)

def poista_pelaaja(juomarit, poistettava_juomari):
    for juomari in juomarit:
        if juomari.name.lower() != poistettava_juomari.lower():
            break
    juomarit.remove(poistettava_juomari)
    return(juomarit)



def pelaa(juomari):
    numero = np.random.uniform()
    numero = int(np.floor(numero*(len(juomari.juomalista)+juomari.juomat_putkeen)))
    vesi_index = len(juomari.juomalista)-1
    if numero > (vesi_index):
        numero = vesi_index
    juoma = juomari.juomalista[numero]
    juomari.juomat_putkeen += 1
    if numero == vesi_index:
        juomari.juomat_putkeen = 0
        juomari.vedet += 1
    else:
        juomari.juomat += 1
    return(juomari)
