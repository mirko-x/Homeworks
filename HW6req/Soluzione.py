#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images

'''def ruota_dx_90(img,tile_size):
    img_dx_90( = [ [ () ]* tile_size for riga in range(tile_size) ]
    for y, riga in enumerate(img):
        for x, pixel in enumerate(riga):
            X = tile_size - 1 - y
            Y = x
            img_dx_90([Y][X] = pixel

    return img_dx_90

 
for rigaq in img_1[riga:riga+tile_size] :
        q1.append(rigaq[quad:quad+tile_size]) '''
 
     
def ruota_sx_90(img,tile_size):
    '''img_sx_90 = [ [ () ]* tile_size for riga in range(tile_size) ]  #non mi serve calcolarlo per ogni tassello edit non mi serve propr
       for y in range(tile_size):
         for x in range(tile_size):
            img_sx_90[tile_size -1 -x][y] = img[y][x]'''
   
    #return [ [ img[x][y] for x in range(tile_size)] for y in range(tile_size - 1, -1,-1)]
    return list(map(list,zip(*[riga[::-1] for riga in img])))


def file(key,encrypted_file,plain_file) :
    
    chiavi="".join(key)
    keylen=len(chiavi)
    with open(encrypted_file , "r", encoding="utf-8")  as f :   
      text= [carattere for carattere in f.read()]
      
    n=len(text)
    for i in range(n):
        pos=i%keylen
        if chiavi[pos] =="N":continue
        
        elif (chiavi[pos]) == "R":
             text[i]=chr(ord(text[i])+1)
       
        
        elif (chiavi[pos]) == "F":
              if i+1 < n:  text[i],text[i+1]  = text[i+1],text[i]
              else:   text[-1],text[0]=text[0],text[-1]
              
        else:   text[i]=chr(ord(text[i])-1)

    with open(plain_file , "w", encoding="utf-8")  as f :   
      f.write("".join(text))
    

 
def jigsaw(puzzle_image: str, plain_image: str, tile_size:int, encrypted_file: str, plain_file: str) -> list[str]:
    img_1=images.load(puzzle_image)
    img_2=images.load(plain_image)
    h,w=len(img_1),len(img_1[0])
    stringa=""
    #img_sx_90 = [ [ None ]* tile_size for _ in range(tile_size) ]   
    #img_sx_90= [ _ for _ in (map(lambda x : [()]*tile_size,range(tile_size)))]  piu costoso
    for riga in range(0,h,tile_size):
        stringa+=(" ")
        for quad in range(0,w,tile_size):
            q1=[rigaq[quad:quad+tile_size] for rigaq in img_1[riga:riga+tile_size]]
            q2=[rigaq[quad:quad+tile_size] for rigaq in img_2[riga:riga+tile_size]]
            if q1==q2 :stringa+= "N"
            elif  [riga[::-1] for riga in q1][::-1] == q2 : stringa+="F"  
            elif  ruota_sx_90(q1,tile_size)==q2: stringa+="L"
            else: stringa+="R"

    key=stringa.split(" ") 
    del key[0]

    file(key,encrypted_file,plain_file)
      
    return key 
    pass


