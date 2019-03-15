
#!/usr/bin/env python

import socket
from random import randint

serversocket    =   socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creamos socket

serversocket.bind(('10.108.33.32', 8080)) #Mantenemos en esucucha el puerto (8000)

serversocket.listen(1) #Mantenemos en escucha el servidor

clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
print ('Conexion desde: ', clientaddress)  #Imprimir la IP del clientsocket

clientaddress=list(clientaddress)
clientaddress.pop(1)
clientaddress=clientaddress[0]
num_sep=clientaddress.split(".")
suma = int(num_sep[0])+int(num_sep[1])+int(num_sep[2])+int(num_sep[3])
resto=str(suma%10)

#Entra en el bucle mientras se mantenga la conexión
try:
    while 1:
        numero=str(randint(0,9))

        if numero == resto:
            newdata = str.encode('TE HA TOCADO EL NUMERO ERA ') #Escribimos la respuesta
            newdata_2=str.encode(numero)
            clientsocket.send(newdata) #Envia la respuesta del servidor
            clientsocket.send(newdata_2)

        elif numero != resto:
            newdata = str.encode('NO TE HA TOCADO EL NUMERO ERA ')#Escribimos la respuesta
            newdata_2=str.encode(numero)
            clientsocket.send(newdata)
            clientsocket.send(newdata_2)

        serversocket.listen(1) #Mantenemos en escucha el servidor
        clientsocket, clientaddress = serversocket.accept()  #Aceptamos la conexión
        print ('Conexion desde: ', clientaddress)  #Imprimir la IP del clientsocket

    clientsocket.close() #Cierra el socket

except KeyboardInterrupt:
        print()
        print("Ejecución interrumpida por el usuario.")
        print("El programa ha finalizado.")
        clientsocket.close()
