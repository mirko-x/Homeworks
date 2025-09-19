#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Consideriamo la codifica posizionale di un numero in base B.
Date le N cifre:      a_{N-1} .... a_1 a_0
Il valore del numero si ottiene sommando, per ogni indice i
da 0 ad N-1, i valori a_i*B^i .

Esempio: se la base B=6  e il numero è     (52103)_6
Il suo valore sarà    5*6^4 + 2*6^3 + 1*6^2 + 0*6^1 + 3*6^0 = (6951)_10

Generalizziamo questa notazione per usare basi diverse per ciascuna
posizione: avremo quindi una lista "bases" formata da N basi e un
numero formato da N cifre contenute in una lista di nome "digits".
Per l'esempio sopra avremo: bases = [6, 6, 6, 6, 6] digits = [5, 2, 1,
0, 3]. Le cifre sono tali che ciascuna sia minore della base nella
stessa posizione.  Il valore del numero in base 10 si ottiene come
nella conversione iniziale, usando per la potenza i-esima la base
i-esima della lista.

NOTA: per comodità useremo nel codice delle liste di cifre e di basi
in cui l'esponente della potenza corrisponde all'indice nelle liste.
Quindi ciascuna lista conterrà basi e cifre a partire dalle unita'.

NOTA: Il numero di basi N e' maggiore stretto di 1. I valori delle
basi anche esse sono maggiori di 1.

In base a quanto detto, data in ingresso una lista "bases",
un obiettivo dell'HW e' genera la lista di tutte le possibili
combinazioni valide di cifre rappresentabili con quelle basi.

Esempio: se in ingresso bases vale [2, 5], tutte le combinazioni sono:
[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4]]

infatti:
- nella prima cifra ci sono solo valori fra [0, 1] perche' la base e' 2
- nella seconda cifra ci sono solo valori fra [0, 4] perche' la base e' 5.

Ciascuna combinazione rappresenta un intero che va convertito da lista
a intero secondo la base specificata in "bases". Una volta che tutte
le possibili combinazioni sono state convertite in un intero e'
necessario trovare quali interi hanno piu di una rappresentazione
nelle basi date.

Esempio: Se in ingresso bases vale [4, 3, 2] allora gli interi che 
ammetto piu di una rappresentazione sono {3, 4, 5, 6, 7, 8, 9, 10}

Infatti, ad esempio il numero 10 con queste basi ha le due rappresentazioni 
    [3, 1, 1] -> 3*4^0 + 1*3^1 + 1*2^2 = 10
    [0, 2, 1] -> 0*4^0 + 2*3^1 + 1*2^2 = 10

Il problema e' gia' stato diviso in sottoproblemi e dovete realizzate
quindi le funzioni che seguono:
 - decode_digits, e' la funzione piu semplice e basilare che riceve
   una lista di basi e una lista di digits e la converte in intero.
 - generate_digits, e' la funzione che fa la maggior parte del lavoro
   che data una lista di basi, calcola tutte le combinazioni.
 - find_doubles, e' l'ultima funzione che date le combinazioni trova i
   corrispettivi interi che hanno piu di una rappresentazione.

Il Timeout applicato è 0.5 secondi.

ATTENZIONE: è vietato importare altre librerie oltre quelle già presenti.
"""
from typing import List, Set

def decode_digits(digits: List[int], bases: List[int]) -> int:
    n=len(bases)
    val=0
    for i in range(n):
       val+=(digits[i]*(bases[i]**i)) 
    return val

def generate_digits(bases : List[int] ) -> List[List[int]]:
    n=len(bases)
    digits=[]
    if n==1:
      digits = [[x] for x in range(bases[0])]
        
    elif n==2:
      digits = [[x, y] for x in range(bases[0]) for y in range(bases[1])]
      
   
    else :
        comb=[0]*n
        while comb[0]<bases[0]:
              digits.append(comb.copy())
              comb[-1]+=1
              for x in range(n-1,0,-1):
                  if comb[x]==bases[x]:
                     comb[x]=0
                     comb[x-1]+=1  
                  else: break
    return digits


def find_doubles(bases : List[int]) -> Set[int]:

   digits = generate_digits(bases)
   nodup = set()
   doubles = set()
   for lst in digits:
       intero = decode_digits(lst, bases)
       if intero  in nodup:
           doubles.add(intero)
       else:
           nodup.add(intero)
   return doubles


###################################################################################
if __name__ == '__main__':
    pass
    # inserisci qui i tuoi test
    # se vuoi provare il tuo codice su piccoli dati
    # nota per eseguire questo main devi usare program.py
    # come cliente e non come modulo ossia con python program.py  
