# Loading question and answer from text file
from ast import Or
from operator import or_, truediv
from pickle import FALSE, TRUE

def load_qna():
    questions = []
    answers = []
    with open('QNA.txt') as text:
        for line in text.readlines():
            split = line.split("--")
            questions.append(split[0])
            answers.append(split[1])
        text.close
    return questions, answers

def process(i):
    status = TRUE
    err_message = "Sorry I can't understand your question!"
    while (status == TRUE):
        if (i.lower() == load_qna()[0][0].lower() or "hours" in i.lower()):
            print(load_qna()[1][0] + "\nDo you have anymore questions ?")
            index = input()
            if index == "no":
                status = FALSE
            elif index=="yes":
                print("hi what can i help you with ?")
                message=input()
                process(message)
        elif (i.lower() == load_qna()[0][1].lower() or "ship" in i.lower()):
            print(load_qna()[1][1] + "\nDo you have anymore questions ?")
            index = input()
            if index == "no":
                status = FALSE
            elif index=="yes":
                print("hi what can i help you with ?")
                message=input()
                process(message)
        elif (i.lower() == load_qna()[0][2].lower() or "contact" in i.lower()):
            print(load_qna()[1][2] + "\nDo you have anymore questions ?")
            index = input()
            if index == "no":
                status = FALSE
            elif index=="yes":
                print("hi what can i help you with ?")
                message=input()
                process(message)
        elif (i.lower() == load_qna()[0][3].lower() or "help" in i.lower()):
            print(load_qna()[1][3] + "\nDo you have anymore questions ?")
            index = input()
            if index == "no":
                status = FALSE
            elif index=="yes":
                print("hi what can i help you with ?")
                message=input()
                process(message)
        else:
            return err_message



if __name__ == '__main__':
    print("hi what can i help you with ?")
    message = input()
    process(message)




