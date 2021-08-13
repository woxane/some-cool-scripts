#!/usr/bin/python3

import threading
import socket
import sys

server_config = ("127.0.0.1" , int(sys.argv[1]))

server_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
server_socket.bind(server_config)
server_socket.listen()

try : 
    password = sys.argv[2]
    password_exist = True
    print(f"the password is : {password}")
except : 
    password_exist = False

clients = [] 
clients_name = []

def broadcast(msg , cl=None) : #cl means client :") 
    for client in clients : 
        if client is not cl : 
            client.send(msg.encode())



def get_message(client) : 
    while True : 
        message = client.recv(1024).decode()
        print(message)

        broadcast(message , client) 



def join_client() : 
    while True : 
        client , client_info = server_socket.accept()
        print(f'{client_info} has joined into the server')

        if password_exist : 
            client.send("password".encode())
            if client.recv(1024).decode() == password :
                client.send("1010".encode())
                name = client.recv(1024).decode() 
                clients_name.append(name)
                print(f"{name} has joined into the chat")
                clients.append(client)
                client.send("you are connected into the chat".encode())
                threading.Thread(target=get_message , args=(client ,)).start()
            else : 
                client.send("wrong password".encode())
                client.close()
                print(f"{client_info} has kicked . (wrong password)")

        else : 
                client.send("1010".encode())
                name = client.recv(1024).decode() 
                clients_name.append(name)
                print(f"{name} has joined into the chat")
                clients.append(client)
                client.send("you are connected into the chat".encode())
                threading.Thread(target=get_message , args=(client ,)).start()

if __name__ == "__main__" : 
     while True:
        try:
            with open('hello.txt', 'a') as f:
                pass
            print("server start ...")
            join_client()
        except:
            print("connection loss ...")           

