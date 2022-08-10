#!/usr/bin/python3

from os import listdir , rename


class Main : 
    def __init__(self , VidExt , SubExt)  :
        self.VidExt = VidExt
        self.SubExt = SubExt 
        self.GetFiles() 
    
    def GetFiles(self) :   
        FilesList = listdir()
        self.Videos = [Vid[ : Vid.find] for Vid in FilesList if Vid[Vid.find('.') : ] == self.VidExt]
        self.Subtitle = [Sub for Sub in FilesList if Sub[Sub.find('.') : ] == self.SubExt ] 

        if self.Video : 
            self.Rename()
   
   def Rename(self) : 
        for i in range(len(self.Videos)) :  
            Sub = self.Subtitle[i] 
            Vid = self.Videos[i] 
            print(Vid) 
            print(Sub)
            rename(Sub+'.'+self.SubExt , Vid+'.'+self.SubExt)

    

    def Help(self) : 
        print('There is fucking help doc hihi ha :) ') 



if __name__ == "__main__" : 
    VidExt = input('Enter your video extension (WIHTOUT DOT) : ')
    SubExt = input('Enter your subtitle extension (WIHTOUT DOT) : ')
    Main = Main(VidExt , SubExt) 
