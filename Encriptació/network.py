# -*- coding: utf-8 -*-
"""
Created on Wed Feb 24 20:52:04 2021

@author: Marina
"""

''' Prova multiplayer online 2'''

import socket

class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server= "192.168.0.26"
        self.port= 5555
        self.addr = (self.server, self.port)
        self.pos = self.connect() #ha posat self.pos
        #print(self.pos)
        
    def connect(self): #Per mirar que estigui conectat i a on
        try: #Això és perquè si no va, que continui executant, em sembla
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
        
        
    def send(self, data): #Per enviar informació (data)
        try:
            self.client.send(str.encode(data)) 
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
            
    def getPos(self): #Això em retorna si està connectat o no?
        return self.pos
        

#n = Network()

#print(n.send("43,53"))
#print(n.send("53,63"))
