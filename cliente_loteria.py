#!/usr/bin/env python

import socket


clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #Crear el socket

clientsocket.connect(('10.108.33.32',8080)) #Se conecta al servidor (IP,puerto)

#Entra en el bucle si está conectado
while 1:
        newdata = clientsocket.recv(1024).decode()  #Recibe la respuesta del servidor
        print ('servidor: %s' % newdata) #Imprime la respuesta
        break
clientsocket.close()  #Cierra el socket
