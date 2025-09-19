#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Il tuo caro amico Pico de Paperis ti ha mandato un messaggio molto strano scarabocchiato su una cartolina.
Ê da tanto che non lo vedi e da sempre vi divertite a scrivervi in codice.
Per decodificare il suo messaggio vai a cercare nella tua biblioteca un libro un po' particolare,
il cifrario di Archimede Pitagorico. Il cifrario da applicare è la famosa "Cifra del Faraone".
La decifrazione col metodo del Faraone si basa su delle regole di sostituzione di sequenze di simboli nel testo.
Il motivo per cui si chiama "cifra del Faraone" è che in antico Egizio le sequenze formate da più geroglifici
potevano essere scritte in qualsiasi ordine, quindi ogni anagramma delle sequenze era valido.
Per rendere la cosa più strana, Pico de Paperis ha deciso di usare un cifrario che non è esattamente quello del
Faraone, ma una sua variante. Invece di usare gli anagrammi usa dei "quasi anagrammi", cioè anagrammi che nel testo
originale hanno un carattere spurio in più rispetto alla sequenza cercata.
Nel cifrario sono contenute coppie di sequenze che indicano come trasformare il testo.
Ad esempio la coppia 'shampoo' -> 'soap' corrisponde a cercare un punto del messaggio in cui appare la sequenza 'shampoo'
(o un suo anagramma) ma con un carattere in più (ad esempio 'pmQohaso') e sostituirla con la sequenza 'soap'.

La decodifica del messaggio può portare a più possibili messaggi finali, perchè possono esserci più sequenze nel testo
che possono essere trasformate in ogni momento e l'ordine delle trasformazioni influenza le trasformazioni successive.
Ad un certo punto succederà che nessun "quasi-anagramma" delle sequenze del cifrario è presente in nessun punto
della sequenza di simboli per cui non è più possibile fare trasformazioni.
Queste sequenze le chiamiamo sequenze finali.
Di tutte le possibili sequenze finali,ci interessa l'insieme delle più corte.
RICORSIVAMENTE calcolare tutte le possibili foglie dell'albero con radice la sequenza criptata 

Per decodificare il messaggio di Pico de Paperis devi implementare la funzione 
pharaohs_revenge(encrypted_text : str, pharaohs_cypher : dict[str,str]) -> set[str]: 
che riceve come argomenti:
- il testo che ti ha mandato Pico de Paperis, come stringa di simboli (caratteri)
- il cifrario da applicare, un dizionario che ha come chiavi le sequenze di cui cercare nel testo un quasi-anagramma
   e come valore associato la stringa da sostituire al quasi-anagramma trovato.
la funzione deve tornare l'insieme dei più brevi testi ottenibili applicando ripetutamente
le trasformazioni fin quando non è più possibile applicarne nessuna.

Esempio:
encrypted_text  = 'astronaut-flying-cyrcus'
pharaohs_cypher = {'tuar': 'me', 'cniy': 'op', 'sorta': 'tur', 'fult': 'at', 'rycg': 'nc'}

Risultato: ['tmeopcus', 'metopcus', 'ameopcus', 'atmepcus']
e tutte le trasformazioni applicate sono quelle contenute nel file example.txt
(in ordine alfabetico e senza ripetizioni)

NOTA: almeno una delle funzioni o metodi che realizzate deve essere ricorsiva
NOTA: la funzione/metodo ricorsivo/o deve essere definita a livello più esterno
      altrimenti fallirete il test di ricorsione.
'''


def AnagrammaS(string, key):
     #if  any(char not in string for char in key ): return False
     keylist=[]
     for char in key :
         if char in string :
             keylist.append(char)
         else: return False
         
     liststring = [char for char in string ]
     
     for char in keylist:
         if char in liststring:
             liststring.remove(char)

     return len(liststring) == 1  


    
def ric(encrypted_text, pharaohs_cypher, tree,ripetuti):
    if  encrypted_text  in ripetuti :
        return tree 
    else: ripetuti.add(encrypted_text)
    
    criptlen=len(encrypted_text) 
    nodi = set()
    flag = True
    
    for key in pharaohs_cypher:
        keylen = len(key)
        for i in range(criptlen-keylen):
            string = (encrypted_text[i:i+keylen+1])
            if    AnagrammaS(string,key)  :
                flag = False
                # newstring=encrypted_text.replace(string,v)   #piu lento
                nodi.add(encrypted_text[:i] + pharaohs_cypher[key] + encrypted_text[i+keylen+1:]) 
         
    if flag  :
        #tree.add(encrypted_text)          
        return tree + [encrypted_text]
        
    for child in nodi:      
        #tree.update(ric(child, pharaohs_cypher, tree,ripetuti))
        tree = ric(child, pharaohs_cypher, tree,ripetuti)
        
        
    return tree


def pharaohs_revenge(encrypted_text: str, pharaohs_cypher: dict[str, str]) -> set[str]: 
    tree = ric(encrypted_text, pharaohs_cypher,[],set())  # set() <-> []
    n = len(min((tree), key=len))
    return {final for final in tree if len(final) == n}
    pass
    

    
'''
from tree import Tree

def AnagrammaS(string, key):
     #if  any(char not in string for char in key ): return False
     keylist=[]
     for char in key :
         if char in string :
             keylist.append(char)
         else: return False
         
     liststring = [char for char in string ]
     
     for char in keylist:
         if char in liststring:
             liststring.remove(char)

     return len(liststring) == 1 
 
    
 
    
 
def ric(encrypted_text, pharaohs_cypher, tree,ripetuti ):
    if  encrypted_text  in ripetuti :
        return tree 
    else: ripetuti.add(encrypted_text)
    
    criptlen=len(encrypted_text)
    flag = True
    
    for key in pharaohs_cypher:
        keylen = len(key)
        for i in range(criptlen-keylen):
            string = (encrypted_text[i:i+keylen+1])
            if    AnagrammaS(string,key)  :
                flag = False
                tree.AddChildValue((encrypted_text[:i] + pharaohs_cypher[key] + encrypted_text[i+keylen+1:]))
                
    if flag  :
        #return Tree(encrypted_text)
        return tree.AddChildValue(encrypted_text)
        
    for child in tree.children :      
         ric(child.value, pharaohs_cypher, tree,ripetuti)
        
        
    return tree


def pharaohs_revenge(encrypted_text: str, pharaohs_cypher: dict[str, str]) -> set[str]: 
    tree=Tree(encrypted_text)
    tree = ric(encrypted_text, pharaohs_cypher,tree,set())  # set() <-> []
    n = len(min((tree.children), key=lambda x : len(x.value)).value)
    return {final.value for final in tree.children if len(final.value) == n}
    passs
    
'''

if __name__ == '__main__':
    print(pharaohs_revenge("d\ud80c\udc94\ud80c\ude3d\ud80c\ude6f\ud80c\udfdb\ud80c\ude6fE\ud80c\udd7dZ\ud80c\ude3dd\ud80c\udfdb\ud80c\udc94\ud80c\udf7f\ud80c\ude3dgryasso\ud80c\udd7dX\ud80c\udfe2\ud80c\udd0f\ud80c\udd0f\ud80c\ude31\ud80c\udfe2\ud80c\ude6f\ud80c\ude6f\ud80c\udfdb\ud80c\ude6f\ud80c\udd7d\ud80c\udc94\ud80c\udf7f\ud80c\ude3d\ud80c\ude3d\ud80c\ude6f\ud80c\ude31ZXqs\ud80c\udf7f\ud80c\udd7d\ud80c\udc94id\ud80c\udc94\ud80c\udfe2\ud80c\udfe2EE\ud80c\udf7f\ud80c\udc59",
                           {
        "\ud80c\udc94\ud80c\udfe2Z\ud80c\udd0fX\ud80c\udd7d\ud80c\udfe2\ud80c\udd0f\ud80c\ude31\ud80c\udc94\ud80c\udd7d\ud80c\ude6fq": "c\ud80c\udc94h\ud80c\ude3d\ud80c\ude31\ud80c\udc94iq\ud80c\ude3d\ud80c\udc94",
        "\ud80c\udfe2d\ud80c\ude6f\ud80c\udc94\ud80c\udfe2\ud80c\ude31\ud80c\udc94Zd\ud80c\udfdb": "The hun",
        "\ud80c\udc94\ud80c\udf7f\ud80c\udfe2\ud80c\udf7f\ud80c\udc59\ud80c\udfe2\ud80c\udd7dd\ud80c\udc94iE": " hotdog.",
        " \ud80c\udfe2Te\ud80c\udfdb\ud80c\udc94\ud80c\ude6f": "d\ud80c\udfe2nd",
        "\ud80c\udc94o\ud80c\udfe2doh\ud80c\udc59g": "ito d",
        "i\ud80c\udc94\ud80c\udd0f\ud80c\ude6f\ud80c\ude31\ud80c\ude3d\ud80c\udc94\ud80c\udc94Xq": "\ud80c\udc94\ud80c\udc94\ud80c\udfe2\ud80c\udd7d\ud80c\ude31\ud80c\udd0fZ",
        "\ud80c\udc94\ud80c\udc94\ud80c\ude6f\ud80c\udfdbZ\ud80c\ude31\ud80c\udd0fq\ud80c\ude3d\ud80c\udd7d": "\ud80c\ude6f\ud80c\ude6fZ\ud80c\udc94q\ud80c\udf7f\ud80c\udd0f",
        "\ud80c\ude6f\ud80c\udfdb\ud80c\ude6fX\ud80c\ude3d\ud80c\udd7d\ud80c\udc94\ud80c\ude31qZ\ud80c\ude6f\ud80c\ude6f\ud80c\udf7f": "\ud80c\udd0f\ud80c\udc94\ud80c\ude6f\ud80c\udc94Zq\ud80c\udd7d\ud80c\udc94\ud80c\udc59\ud80c\udd0f",
        "\ud80c\ude6f\ud80c\udd7d\ud80c\udfdb\ud80c\ude6fZE\ud80c\ude3d\ud80c\ude3d\ud80c\ude3dd\ud80c\udf7f\ud80c\udc94": "d\ud80c\udc94\ud80c\udfe2\ud80c\udc94\ud80c\ude6f\ud80c\ude31Z\ud80c\udfe2\ud80c\udfdb",
        "\ud80c\ude31\ud80c\udc94i\ud80c\udc59h\ud80c\ude3d\ud80c\ude3d\ud80c\udd0f\ud80c\udc94\ud80c\udc94q": "iate zip",
        "\ud80c\udd7dZ\ud80c\udc94\ud80c\ude6f\ud80c\ude3d\ud80c\ude6f\ud80c\ude3dZ\ud80c\ude6f": "\ud80c\udc94\ud80c\ude3dZ\ud80c\ude3d\ud80c\udfe2\ud80c\udc94",
        " \ud80c\udc94\ud80c\udc94q\ud80c\ude3dz\ud80c\udc94t": "z\ud80c\ude3ditq"
    }))
    pass
