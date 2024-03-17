file1 = open("Questions.txt", "r+") 
list = file1.readlines()
file1.close

def AddQuestion():
    file1 = open("Questions.txt", "r+")
    Question = input("Please enter your question. \n")
    Answer = input("Please enter the answer to your question. \n")

    print("The question and answer you entered in:  Q: " , Question , "  A:  " , Answer)
    print("\n")
    MenuChoice1 = input("Is this question and answer correct?  (Y/N)")
    MenuChoice1 = MenuChoice1.upper()

    if MenuChoice1 == "Y":
        MenuChoice2 = input("Do you wich top save your new question to the Questions file?")
        MenuChoice2 = MenuChoice2.upper()
        if MenuChoice2 == "Y":
            file1 = open("Questions.txt", "a") 
            file1.write(Answer + ":" + Question + "\n")
            file1.close
    else:
        print("Please try again.")


def AskingQuestions(SubList, SubLen):
    score = 0
    for i in range(0,SubLen):
        question = SubList[i]
        question = question.split(':')
        #print(i)

        UserAnswer = input(question[1] + "? ")
        UserAnswer = UserAnswer.upper()
        #print(UserAnswer)

        ProgAnswer = question[0]
        ProgAnswer = ProgAnswer.upper()
        #print(ProgAnswer)

        if UserAnswer == ProgAnswer:
            print("Correct")
            score = score + 1
        else:
            print("Incorrect")

    #print(i)
    print(score)

Len = len(list)


#Main Program - Menu Menu
AddQuestion()
#AskingQuestions(list, Len)


