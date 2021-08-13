#!/usr/bin/python3

import socket
import sys
import threading


server_config = (sys.argv[1] , int(sys.argv[2]))
client_socket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
client_socket.connect(server_config)

name = input("Enter your name : ")
stop_thread = False

def get_message() : 
    while True : 
        global stop_thread 
        if stop_thread :
            break

        try : 
            message = client_socket.recv(1024).decode()
            if message == "password" : 
                client_socket.send(input("Enter the password : ").encode())

            elif message == "wrong password" :
                print("wrong password")
                sys.exit()

            elif message == "1010" : 
                client_socket.send(name.encode())
            
            elif message != "" : 
                print(message) 
            

        except : 
            client_socket.close()
            stop_thread = True 
            break


def send_message() : 
    while True : 
        if stop_thread : 
            break 

        message = f"{name} : {input('you : ')}"

        client_socket.send(message.encode())


send = threading.Thread(target = send_message)
get = threading.Thread(target = get_message)

get.start()
send.start()

