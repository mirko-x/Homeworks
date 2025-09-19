#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

def traduzione(riga : str) :
    setg=frozenset({"b","#"}) 
    if "b" in riga or "#" in riga:
        note=[]
        for x in riga:
           if  x in setg :
              note[-1] += x
           else : 
              note.append(x)

        return note
 
    else : return riga

def occorrenze (note:list[str] ) -> str :
    trans = []
    count = 1
    n=len(note)
    for i in range(n - 1):
        if note[i] == note[i + 1]:
            count += 1
        else:
            trans.append(f"{note[i]}{count}")
            count = 1

    trans.append(f"{note[-1]}{count}") 
     
    
    return ''.join(trans)  
    
def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
  #use a dictionary with ascii codes :
  '''ascii_dict = {
    48: 65,
    49: 66,
    50: 67,
    51: 68,
    52: 69,
    53: 70,
    54: 71,
    45: 98,  
    43: 35,  
    32: 80   
  }'''
  songs={}
  result={}
  f=open(os.path.join(source_root, "index.txt"))
  testo=f.readlines()
  f.close() 
  #songs = { linea.strip("\n").strip('"').split('" "')[0] : linea.strip("\n").strip('"').split('" "')[1] for linea in testo}
  for linea in testo :
       titolo, path = linea.strip("\n").strip('"').split('" "')
       songs[titolo]=path    
   
    
  for titolo , path in songs.items():
    directory = os.path.dirname(path)
    if directory:
      os.makedirs(os.path.join(target_root, directory),exist_ok=True)
    else: 
      os.makedirs(target_root,exist_ok=True)
  
    file=open(os.path.join(source_root , path)) 
    text=file.read()
    file.close()
    
    text=text.translate(str.maketrans("0123456-+ " ,"ABCDEFGb#P" ))
    #text=text.translate(ascii_dict)
    note=[]
    for riga in text.split("\n") :
          note.extend(traduzione(riga[::-1]))
            
            
    result[titolo] = len(note)    
    
    tradotto=occorrenze(note)
    
    filew= open(os.path.join(target_root, directory, titolo + ".txt"), "w") 
    filew.write(tradotto)
    filew.close()
  

  index=''.join(map(lambda tupla: f'"{tupla[0]}" {tupla[1]}\n',sorted(result.items(), key=lambda x: (-x[1], x[0]))))           
  fileindx=open(os.path.join(target_root, "index.txt") ,"w" ) 
  fileindx.write(index)
  fileindx.close()
                          
  return result
  pass
    
 
