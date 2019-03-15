import numpy as np
import os
import textwrap
import sys

def lisaa_pelaaja(juomarit, uusi_juomari):
    for juomari in juomarit:
        if juomari.name.lower() == uusi_juomari.lower():
            break
    new_juomari = juomari()
    new_juomari.name = uusi_juomari
    juomarit.append(new_juomari.lower())
    return(juomarit)

def lisaa_juoma(juomari, uusi_juoma):
    for juoma in juomari.juomalista:
        if juoma.lower() == uusi_juoma.lower():
            break
    juomari.juomalista.append(uusi_juoma.lower())
    return(juomari)

def poista_pelaaja(juomarit, poistettava_juomari):
    for juomari in juomarit:
        if juomari.name.lower() != poistettava_juomari.lower():
            break
    juomarit.remove(poistettava_juomari)
    return(juomarit)

def poista_juoma(juomari, poistettava_juoma):
    for juoma in juomari.juomalista:
        if juoma.lower() == poistettava_juoma.lower():
            break
    juomari.juomalista.remove(poistettava_juoma.lower())
    return(juomari)

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
