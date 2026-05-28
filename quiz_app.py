import json
import random
import time
from colorama import Fore, Style, init
init()

def category():
        print("Choose a category.")
        print("1. Movies")
        print("2. General Knowledge")
        print("3. Science")
        print("4. Sports")
    
        choice= int(input("Enter your choice's number:"))
        if choice== 1:
            return "movies"
        elif choice== 2:
               return "general knowledge"
        elif choice== 3:
               return "science"
        elif choice== 4:
                return "sports"           

def difficulty():
        print("Choose a Level")
        print("Easy")
        print("Medium")
        print("Hard")
        choice = input("enter your choice=")
        return choice  

def get_questions(categories,level):
       global points
       f = open("questions.json", "r")
       L = json.load(f)
       random.shuffle(L)
       for i in L:
              if i["category"]== categories and i["difficulty"]== level :
                     print(i["question"])
                     for j in i["options"]:
                            print(j)
                     start = time.time()       
                     answer= input("Enter your answer=")
                     end = time.time()
                     time_taken = end - start
                     if answer == i["answer"]:
                            points+=1
                            print("points","=",points,Fore.GREEN + "Yay! correct option." + Style.RESET_ALL,"time taken", time_taken , "seconds")
                     else:
                            print(Fore.RED + "Wrong Answer!" + Style.RESET_ALL)  
                            print("Right answer is=", i["answer"]) 
       f.close()           
                          

points=0
start = input(" TO  start the game type Yes=")
while start == "yes" or "Yes":
      categorise = category()
      level = difficulty()
      get_questions(categorise, level)
      play_again = input("Do you want to continue? (yes/no): ")
      if play_again.lower() == "no":
        print(f"Game Over! Final Score: {points}")
        break              


       
       


