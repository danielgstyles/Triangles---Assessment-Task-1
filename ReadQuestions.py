file1 = open("Questions.txt", "r+") 
list = file1.readlines()
print(list)

print(list[0])
question = list[0]
question = question.split(':')
print(question)
len = len(list)

#print(len)
i = 0
while i < len:
    question = list[i]
    question = question.split(':')
    #print(i)
    answer = input(question[1] + " ")
    if answer == question[0]:
        print("Correct")
    i =i+1
    print(i)