from re import I
import words_manager
import user_manager
from datetime import datetime
from os import path
from time import sleep

def start(username):
    user_manager.userlogin(username)
    userdb = open("userdb.txt" , "r" )
    for i in userdb:
        if username in i:
            username , language, word_amount = i.split()
            word_amount = int(word_amount)
            print(username , language, word_amount)
    words = words_manager.get_words(word_amount,language)
    print("   ",*words)
    sleep(1)
    start_time = datetime.now()
    userinput = input("GO!!")
    finish_time = datetime.now()


if __name__ == '__main__':
    username = input("enter your username ")
    start(username)