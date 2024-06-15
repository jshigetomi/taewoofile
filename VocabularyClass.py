import os
import random

class Vocabulary():
    def __init__(self):
        self.englishlist = []
        self.koreanlist = []
        self.correct = 0
        self.total = 0
        self.languageChoice = 'undecided'
        self.testlang = []
        self.answerlang = []

    def initlist(self,path):
        with open(path,"r",encoding="utf-8") as file:
            lines = file.readlines()
            self.total = len(lines)
            for words in lines:
                eng,kor = words.split(":")
                self.englishlist.append(eng.strip())
                self.koreanlist.append(kor.strip().split(","))
                

    def test(self):
        while True:
            os.system('cls')
            choice = input("Do you want to start? (yes/no)")
            if choice == 'yes':
                self.begintest()
                break
            elif choice == 'no':
                break
            else:
                input("Please enter yes or no")

    def begintest(self):
        self.langchoice()
        indices = list(range(len(self.testlang)))
        random.shuffle(indices)
        self.testlang = [self.testlang[i] for i in indices]
        self.answerlang = [self.answerlang[i] for i in indices]
        for index in range(0,len(self.testlang)):
            os.system('cls')
            print("You are on word #" + str(index + 1) + " out of " + str(len(self.testlang)))
            print("You got " + str(self.correct) + " correct.")
            print(self.testlang[index])
            userinput = input("Please translate the word: ")
            if self.checkanswer(userinput, self.answerlang[index]):
                self.correct += 1
                input("You got it correct!")
            else:
                input("That was wrong")
        
        self.displayresults()

    def langchoice(self):
        while True:
            os.system('cls')
            choice = input("Would you like to be tested in Korean or English? (kor/eng)")
            if choice == 'kor':
                self.languageChoice = 'kor'
                self.testlang = self.koreanlist
                self.answerlang = self.englishlist
                break
            elif choice == 'eng':
                self.languageChoice = 'eng'
                self.testlang = self.englishlist
                self.answerlang = self.koreanlist
                break
            else:
                input("Please enter kor or eng.")

    def checkanswer(self, userinput, answer):
        if self.languageChoice == 'eng':
            for word in answer:
                print(userinput + " " + word)
                if userinput == word.strip():
                    return True
            return False
        elif self.languageChoice == 'kor':
            if answer == userinput:
                return True
            else:
                return False
    
    def displayresults(self):
        os.system('cls')
        input(
            "You got " + str(self.correct) + " correct out of " + str(self.total) + ".\n"
            + "For a score of " + str(self.correct/self.total*100) + ".\n"
              )
