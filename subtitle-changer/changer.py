#!/usr/bin/python3

from os import listdir , rename
from sys import argv 

class Main : 
    def __init__(self , VidExt , SubExt)  :
        self.VidExt = VidExt
        self.SubExt = SubExt 
        self.GetFiles() 
    
    def GetFiles(self) :   
        FilesList = listdir()
        self.Videos = [Vid[ : Vid.find('.')] for Vid in FilesList if Vid[Vid.find('.') + 1 : ] == self.VidExt]
        self.Subtitle = [Sub[ : Sub.find('.')] for Sub in FilesList if Sub[Sub.find('.') + 1 : ] == self.SubExt ] 

        if len(self.Videos) >= len(self.Subtitle) : 
            if len(self.Videos) == 0 : 
                print('There is no file with this extenstion')
            else : 
                self.Rename()
   
    def Rename(self) : 
        for i in range(len(self.Videos)) :  
            Sub = self.Subtitle[i] 
            Vid = self.Videos[i] 
            print(Vid) 
            print(Sub)
            rename(Sub+'.'+self.SubExt , Vid+'.'+self.SubExt)

    

    def Help(self) : 
        print('There is not fucking help doc hihi ha :) ') 



if __name__ == "__main__" : 
    VidExt = argv[1]
    SubExt = argv[2]
    Main = Main(VidExt , SubExt) 
