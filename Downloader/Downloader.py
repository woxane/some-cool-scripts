#!/usr/bin/python3

import requests
from sys import argv
from tqdm import tqdm 
from bs4 import BeautifulSoup 
from os import path , system , listdir



    
class Main : 
    def __init__(self) :  
        self.Clear()
        self.FlagCheck()
        self.PrintLinks()
        self.Download()

    def Clear(self) :
        system('clear') 

    def Filter(self , Keywords) : 
        for Keyword in Keywords : 
            self.Links = list(filter(lambda Link : Keyword in str(Link) , self.Links)) 


    def Request(self) : 
        Req = requests.get(self.Url)  
        Soup = BeautifulSoup(Req.text , 'html.parser') 
        self.RequestCheck(Req.status_code) 

        self.Links = list(filter(lambda Link : 'dl' in str(Link) , [Link_.get('href') for Link_ in Soup.find_all('a')])) # If this piece is unclear for you just get over it :)

        if self.Keywords :  # if self.Keywords have any element
            self.Filter(self.Keywords) 

    def RequestCheck(self , StatusCode) : # Check if the request status code is 200 or not  
        if StatusCode == 200 : 
            pass

        else : 
            print('An unknown Error Has Accoured !')
    
    def FlagCheck(self) : 
        for arg in argv[1:] :
            if 'url' in arg : 
                self.Url = arg[arg.find('=') + 1 :]

            if '-f' in arg : 
                self.Keywords = arg[arg.find('=') + 1 : ].split(',') # Convert '-f=1080,foo,boo' to ['1080' , 'foo' , 'boo'] 

            elif '-h' in arg : 
                self.Help() 
        
        self.Request()





    def PrintLinks(self) : 
        print('\n'.join(self.Links))

    def Download(self) : 
        input("start ? : ")
        ListDir = os.listdir()

        for Link in self.Links : 
            FileName = path.basename(Link)

            if FileName in ListDir : 
                print('This file has been already downloaded . ') 

            else : 
                Responce = requests.get(Link , stream = True ) 
                FileSize = int(Responce.headers.get("Content-Length", 0))
                Progress = tqdm(url_response.iter_content(1024), f"Downloading {file_name}", total=file_size, unit="B", unit_scale=True, unit_divisor=1024)

                with open(FileName, "wb") as File : 
                    for Data in Progress.iterable : 
                        File.write(Data) 
                        Progress.update(len(data))


    def Help(self) : 
        print('''
                Usage : downloader [OPTIONS] url=[URL]

                Options : 
                    General Options :
                    -h                                              Print this help text and exit
                    -f                                              Filter the output with your options ''') 


if __name__ == '__main__' : 
    Main = Main()   
    Main
