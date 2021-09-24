#!/usr/bin/python3


from sys import argv
import pickle

if argv[1] in ("-h" , "--help")  : 
    print("-h , --help : \n\tHelp documentation .\n-nd , --newDirectory : \n\t For creating new direcroty(movie name).\n\t\tExample : \n\t\t\t python reminder.py -nd Money-Heist\n-ae , --addEpisode : \n\tadding the last episode that you watch . \n\t\tExample : \n\t\t\t python reminder.py -ae Money-heist 5 .\n\t\t\t this add you episode 5 to Money-heist direcroty\n-wa --watchedMovies :\n\t This command show you all watched series of your Directory .\n\t\tExample : \n\t\t\t python reminder.py -wa Money-heist")


elif argv[1] in ("-nd" , "--newDirectoy") :
    try  :
        with open(".data" , "rb") as file : 
            with open(".data" , "wb") as file_w : 
                data = pickle.load(file)
                data[argv[2]] = ""

    except :
        with open(".data" , 'wb') as file : 
            data = {argv[2] : ""} 
            pickle.dump(data , file)


elif argv[1] in ("-ae" , "addEpisode") : 
    with open(".data" , "rb") as file : 
        data = pickle.load(file) 
        with open(".data" , "wb") as file_w : 
            try :
                data[argv[2]] = " "+data[argv[2]]+argv[3]
                pickle.dump(data , file_w)
            except : 
                print("you dont have directory with this name ! .\nPlease read help documentation with python reminder.py -h :>")

elif argv[1] in ("-wa" ,  "--watchedMovies") : 
    with open(".data" , "rb") as file : 
        data = pickle.load(file) 
        try :
            print(data[argv[2]])

        except : 
            print("you dont have this Dircectory . pleases make read help documentation")
