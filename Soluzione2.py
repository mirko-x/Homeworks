#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os


def traduzione(riga : str) :
    setg=frozenset({"b","#"}) 
    riga=riga.translate(str.maketrans("0123456-+ " ,"ABCDEFGb#P" ))       
    riga = riga[::-1]
    note=[]
    if "b" in riga or "#" in riga:
        for x in riga:
           if x in setg :
              note[-1] += x
           else : 
              note += x

        return note
 
    else : return riga

def occorrenze (note:list[str] ) -> str :
    trans = ""
    count = 1
    n=len(note)
    for i in range(n - 1):
        if note[i] == note[i + 1]:
            count += 1
        else:
            #trans += "{0}{1}".format(note[i], count)
            #trans+=(note[i] + str(count))
            trans += f"{note[i]}{count}"            
            count = 1

    trans += f"{note[-1]}{count}"  
     
    
    return trans  

def Umkansanize(source_root:str, target_root:str) -> dict[str,int]:
  songs={}
  result={}
  with open(os.path.join(source_root, "index.txt"),"r",encoding="utf8") as f:
    for linea in f :
       titolo, path = linea.strip("\n").split('" "')
       songs[titolo.strip('"')]=path.strip('"')    
       
  for titolo , path in songs.items():
    directory = os.path.dirname(path)
    target_dir=os.path.join(target_root, directory)
    os.makedirs(target_dir,exist_ok=True)
             
  
    with open(os.path.join(source_root , path),"r",encoding="utf8") as f:
          note=[]
          for riga in f :
              note+= traduzione(riga.strip("\n"))
            
    result[titolo] = len(note)    
    with open(os.path.join(target_dir, titolo + ".txt"), "w", encoding="utf8") as f:
                    f.write(occorrenze(note))
              
  with open(os.path.join(target_root, "index.txt") ,"w",encoding="utf8") as f:
        {f.write(f'"{key}" {value}\n') for key, value in sorted(result.items(), key=lambda x: (-x[1], x[0]))}
        #f.write('\n'.join(map(lambda tupla: f'"{tupla[0]}" {tupla[1]}',sorted(result.items(), key=lambda x: (-x[1], x[0])))))
        #f.write(''.join([f'"{tupla[0]}" {tupla[1]}\n' for tupla in sorted(result.items(), key=lambda x: (-x[1], x[0]))]))
        #for tupla in sorted(result.items(), key=lambda x: (-x[1], x[0])):
              #f.write(f'"{tupla[0]}" {tupla[1]}\n')
        
                          
  return result
  pass
    


