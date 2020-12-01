# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 10:43:04 2020

@author: Marina
"""
import random
import numpy as np

""" Enviament clau"""




def enviament(direccio0,bit0,direccio1,dir0l,bit0l,dir1l,bit1l):
    '''
    Funció que simila l'enviament dels bits i la transformació d'ells

    Parameters
    ----------
    direccio0 : DIRECCIÓ ENVIAMENT (STR)
    bit0 : BIT ENVIAT (INT)
    direccio1 : DIRECCIÓ REBUDA (STR)
    dir0l : LLISTA DE TOTES LES DIRECCIONS DE L'ENVIAMENT
    bit0l : LLISTA DE TOTS ELS BITS ENVIATS
    dir1l : LLISTA DE TOTES LES DIRECCIONS DE LA REBUDA
    bit1l : LLISTA DE TOTS ELS BITS REBUTS

    Returns
    -------
    array0: ARRAY ENVIADA
    array1: ARRAY REBUDA

    '''
    
    #Si es mesura en la mateixa direcció 100% es rebrà igual
    if direccio0==direccio1:
        bit1=bit0
        
    #Si les dues direccions són diferents:   
    else:
        r=random.random()
        if r<=0.5:
            bit1=0
        else: 
            bit1=1
            
    array0,array1=guardar(direccio0,bit0,direccio1,bit1,dir0l,bit0l,dir1l,bit1l)

    return array0,array1



direccio0ll=[]

def guardar(direccio0,bit0,direccio1,bit1,dir0l,bit0l,dir1l,bit1l):    
    '''
    Funció que guarda les direccions i els bits i ho converteix tot en 
    dues arrays: l'enviada i la rebuda'

    Parameters
    ----------
    direccio0 : DIRECCIÓ ENVIAMENT (STR)
    bit0 : BIT ENVIAT (INT)
    direccio1 : DIRECCIÓ REBUDA (STR)
    bit1:   BIT REBUT(INT)
    dir0l : LLISTA DE TOTES LES DIRECCIONS DE L'ENVIAMENT
    bit0l : LLISTA DE TOTS ELS BITS ENVIATS
    dir1l : LLISTA DE TOTES LES DIRECCIONS DE LA REBUDA
    bit1l : LLISTA DE TOTS ELS BITS REBUTS

    Returns
    -------
    array0: ARRAY ENVIADA
    array1: ARRAY REBUDA

    '''
    
    dir0l.append(direccio0)
    bit0l.append(bit0)
    dir1l.append(direccio1)
    bit1l.append(bit1)
    
    array0=np.empty((len(dir0l),2),dtype=str)
    array1=np.empty((len(dir1l),2),dtype=str)
    
    array0[:,0]=dir0l
    array0[:,1]=bit0l
    array1[:,0]=dir1l
    array1[:,1]=bit1l
    
    return array0,array1

        
dir0l=[]
bit0l=[]
dir1l=[]
bit1l=[]   
    
enviament('x',0,'x',dir0l,bit0l,dir1l,bit1l)
enviament('x',1,'z',dir0l,bit0l,dir1l,bit1l)
enviament('z',1,'z',dir0l,bit0l,dir1l,bit1l)
array0,array1=enviament('x',1,'z',dir0l,bit0l,dir1l,bit1l)

print("array enviada",array0)
print("array rebuda",array1)



#%% 
def comparardir(array0,array1):
    array02=np.copy(array0)
    array12=np.copy(array1)
    n,m=np.shape(array0)
    for i in range(n):
        n1,m1=np.shape(array02)
        if i<n1:
           # print('i:',i,'n1:',n1)
            endevant=0
            while(endevant==0):
                n1,m1=np.shape(array02)
                if i<n1:
                    if array02[i,0]!=array12[i,0]:
                       # print('Abans0:',array02[i,0],'i:',i)
                        #print('Abans1:',array12[i,0])
                        array02=np.delete(array02,i,0)
                        array12=np.delete(array12,i,0)
                        #print('Després0:',array02)
                        endevant=0
                    else:
                        endevant=1
                else: 
                    endevant=1
                    break
                
                
        else:
           # print("Anem a fer break")
            break
        
    return array02,array12


arr0=np.array([['x',1],['x',0],['z',0],['x',1]])
arr1=np.array([['z',0],['x',0],['z',0],['z',1]])

arrp,arrp2=comparardir(arr0, arr1)
print("Va bé?",(arrp==arrp2).all())

def escriure(array0,array1):
    
    fw=open("Guardarllistes.txt","w")
    
    dir0l=list(array0[:,0])
    bit0l=list(array0[:,1])
    dir1l=list(array1[:,0])
    bit1l=list(array1[:,1])
    
    #Escric al fitxer les noves llistes
    dir0s=""
    for i in dir0l:
        dir0s+=i
    fw.write(dir0s+"\n")
    
    bit0s=""
    for i in bit0l:
        bit0s+=str(i)
    fw.write(bit0s+"\n")
    
    dir1s=""
    for i in dir1l:
        dir1s+=i
    fw.write(dir1s+"\n")
    
    bit1s=""
    for i in bit1l:
        bit1s+=str(i)
    fw.write(bit1s+"\n")
    
    fw.close()
    
#%%
"Vale, vull fer unes matrius arrays aleatòries d'una mida en concret"

def createarrays(n):
    
    array0=np.empty((n,2),dtype=str)
    array1=np.copy(array0)
    direccions=['x','z']
    bits=['1','0']
    
    for i in range(n):
        array0[i,0]=random.choice(direccions)
        array0[i,1]=random.choice(bits)
        
        array1[i,0]=random.choice(direccions)
        array1[i,1]=random.choice(bits)
        
    
    return array0,array1

#print("Matriu aleatòria", createarrays(15))
    






#%%
def mirarhack(array0,array1):
    if (np.shape(array0)==np.shape(array1)):
        pass
    else:
        print("Les dues matrius no són compatibles")
        
        
    n,m=np.shape(array0)
    #Comparem els 10 primers bits de les arrays que ja s'hagin comparat
    #les direccions
    comptador=0
    '''
    if n<10:
        k=n
    else:
        k=10
    '''
    #Nombre de bits que comparo   
    k=n//10
    print("Valors comparats", k)
    
    for i in range(k):
        if array0[i,1]!=array1[i,1]:
            comptador+=1
           # print("Són iguals?",array0[i,1],array1[i,1])
            print("comptador",comptador)
            
    if comptador>=k//4: #Em mira que 1/4 dels valors siguin iguals, sinó significa que hi ha un hacker!
        print("Hi ha un hacker!")
        return True
        
        
    else: 
        return False
    
arr2,arr3=createarrays(50)
arr22=np.copy(arr2)

boolean=mirarhack(arr2,arr3)
print("Hi ha hacker?",boolean)


print("----------Ara hi ha hacker?", mirarhack(arr2, arr22))    


#%%

"""Primer de tot hem de demenar de quina mida és el missatge que volem enviar"""

missatge=input("Escriu el teu missatge:")

print("Missatge:",missatge)  
longitud=len(missatge)   
print("La longitud del missatge és:", longitud)  

#%%
''' Ara volem saber quants bits necessitarem enviar per transmetre una clau de la mateixa
mida que el missatge. 
Amb 5 bits, podem enviar fins a 32 símbols. Per tant, posem 5 bits per cada número
ja serà suficient.
Per tant haurem d'enviar 5*longitud missatge'''


""" Genial, ara ja sabem quantes partícules haurem d'enviar.
 Ara haurem de procedir a transmetre la clau. Per això utilitzarem les 
 funcions enviament... """
 
def randomprocess(nbits):
    '''
    Funció que a partir del missatge que vulguis enviar, fa tot el procés de
    d'enviar partícules d'spin 1/2 (aleatòries) per tenir la clau de la mateixa
    mida. 

    Parameters
    ----------
    nbits : Nombre de bits que es necessiten per cada número (lletra passada a número)

    Returns
    -------
    finalkey : TYPE
        DESCRIPTION.
    missatge : TYPE
        DESCRIPTION.

    '''

    missatge=input("Escriu el missatge en majúscules: ")

    longitud=len(missatge)   
    print("La longitud del missatge és:", longitud)  
    
    lenkey=nbits*longitud
    
    #Si volem que es rebi una clau de longitud lenkey haurem d'enviar molts mes
    n=int(lenkey*(5/2))
    # n és el nombre de partícules que volem enviar
    
    ''' Per provar-ho, s'enviaran bits 0 o 1 aleatoris en direcció x o z aleatòria'''

    posdir=['x','z']
    posbit=['0','1']
    
    dir0l=[]
    bit0l=[]
    dir1l=[]
    bit1l=[]
    for i in range(n):
        
        arr0,arr1=enviament(random.choice(posdir),random.choice(posbit),random.choice(posdir),dir0l,bit0l,dir1l,bit1l)
        
        #print("array0",arr0)
        #print("array1",arr1)
        
    arr02,arr12=comparardir(arr0,arr1)
    print("--- Procés d'enviament i rebuda de bits---")
    print("S'han enviat",n,"bits dels quals",np.shape(arr02)[0],"ens han aportat informació.")
    #print(arr02)
    #print(arr12)
   
    key=arr02[:,1]
    print('--- Primers bits obtinguts ---')
    print(key)
    while len(key)<lenkey:
        #Tornem-hi, hem d'enviar més bits
        print("S'han d'enviar més bits!")
        for i in range(lenkey):
        
            arr0,arr1=enviament(random.choice(posdir),random.choice(posbit),random.choice(posdir),dir0l,bit0l,dir1l,bit1l)

            
        arr02,arr12=comparardir(arr0,arr1)
        #print(arr02)
        #print(arr12)
    
        key=arr02[:,1]
        print("new key", key, type(key))
        
    #int(i,2)
    finalkeyb=[]
    for i in range(0,lenkey,5):
        num=key[i]+key[i+1]+key[i+2]+key[i+3]+key[i+4]
          
        finalkeyb.append(num)
    
    finalkey=[]
    for i in finalkeyb:
        finalkey.append(int(i,2) )
        
    print('-----Final key-----')
    print("En binari:",finalkeyb)
    print("Decimal:",finalkey)
    return finalkey, missatge
    

clau,missatge=randomprocess(5)

#%%

def Alice(n):
    
    key,message=randomprocess(n)
    
    ''' l'ascii en majúscules va del 65 al 90'''
    
    messagev=[]
    message2=[]
    j=0
    for i in message:
        if ord(i)==32:
            messagev=messagev+[(ord(i)-5+key[j])%27] #tindrà 27
            message2=message2+[ord(i)-5]
        else: 
            messagev=messagev+[(ord(i)-64+key[j])%27]
            message2=message2+[ord(i)-64]

        j+=+1 
    #print('HOLA:',message2)
    #print(messagev)
    message_en=""
    
    for i in messagev:
        if (i==0):
            message_en=message_en+chr(32)
            print('arroba?')
        else:
            message_en=message_en+chr(i+64)
        
    print("---Missatge encriptat amb la clau---")
    print(message_en)
    
    return message_en,key

encriptat,clau=Alice(5)

#%%
def Bob(message_en,key):
    message_out=''
    message_out2=[]
    
    j=0
    for i in message_en:
        
        valor=((27+ord(i)-64-key[j])%27)+64
        if valor==64:
            message_out=message_out+chr(valor-32)
        else:
            message_out=message_out+chr(valor)      
        
        
        message_out2=message_out2+[(27+ord(i)-64-key[j])%27]
        j+=1
    #print('Missatge en numeruus',message_out2)
    print('---Recuperem el missatge inicial---')
    print(message_out)
    return message_out

Bob(encriptat,clau)



    


    
    
    
    