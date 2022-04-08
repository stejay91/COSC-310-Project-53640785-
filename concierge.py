from ast import NodeTransformer
import time
import spacy
import nltk
from nltk.corpus import wordnet
from nltk.sentiment.vader import SentimentIntensityAnalyzer

#the nlp tookit spacy and nltk is used
class Concierge:
    def __init__(self):
        #the spacy is used to do Tokenization, POS tagging and Tokenization.
        #the nltk is used to do sentiment analysis and Synonym recognition.

        self.nlp = spacy.load('en_core_web_sm')
        self.sentiment = SentimentIntensityAnalyzer()
        self.phones = {
            "iPhone 13":999,
            "Samsung Galaxy S22 Ultra":1299,
            "Huawei P50 Pro":899
        }
        self.computers = {
            "MacBook Pro":1299,
            "Alienware":1599,
            "Republic of Game":1499,
            "Dell":799,
            "Samsung":899,
            "Lenovo":799,
            "Asus":999
        }
        self.games = {
            "PlayStation 5":599,
            "Xbox":699,
            "Nintendo Switch":499,
        }
        self.phones_words = {'phone',"mobile"}
        self.computers_words = {"computer","laptop"}
        self.games_words = {"game","play"}

    def concierge_chat(self):
        print("Welcome to our concierge chat service!")
        text = input("How can I help you? (input \'quit\' to leave concierge) ")
        while True:
            if text.lower() == "quit":
                print("Good bye and have a nice day!")
                break
            doc = self.nlp(text)
            #Tokenize the input text
            tokens = [token for token in doc]
            #print(tokens)
            #Tagging the pos of the tokens
            pos = [token.pos_ for token in doc]
            #print(pos)
            noun = []
            #Check if there is any noun inside the input text.
            for i,j in zip(tokens, pos):
                if j == "NOUN":
                    noun.append(str(i))
            synonyms = set()
            #print(noun)
            #Get the synonyms of all nouns.
            for word in noun: 
                for syn in wordnet.synsets(word): 
                    for lm in syn.lemmas(): 
                        synonyms.add(lm.name())
            #print(synonyms)
            works = False
            #If there are any synonyms of computer, phone or game, present the price list of the corresponding products.
            if self.phones_words & synonyms:
                print("Do you want to buy a phone?")
                print("Here are the phones we have now:")
                for i,j in self.phones.items():
                    print(f"Type: {i}, Price: ${j}")
                print()
                works = True
            elif self.computers_words & synonyms:
                print("Do you want to buy a computer?")
                print("Here are the computers we have now:")
                for i,j in self.computers.items():
                    print(f"Type: {i}, Price: ${j}")
                print()
                works = True
            elif self.games_words & synonyms:
                print("Do you want to buy a game console?")
                print("Here are the game consoles we have now:")
                for i,j in self.games.items():
                    print(f"Type: {i}, Price: ${j}")
                print()
                works = True
            
            #Named entity recognition of each token.
            ners = [(ent.text, ent.label_) for ent in doc.ents]
            if ners:
                ners_info = {}
                for i in ners:
                    if i[1] not in ners_info:
                        ners_info[i[1]] = []
                    ners_info[i[1]].append(i[0])
                #print(ners_info)
                reply = ""
                #If there is any geo location inside the text, suggest the user to buy ticket.
                if "GPE" in ners_info:
                    reply = "You may want to go "
                    for i in ners_info["GPE"]:
                        reply += i
                        reply += " or "
                    reply = reply[:-4]
                    reply += '. You can call 000-000-0001 to book the ticket.'
                    print(reply)
                    works = True
                #If there is any art work inside the text, suggest the user to go to the library.
                if "WORK_OF_ART" in ners_info:
                    reply = "You may want to find the work of art "
                    for i in ners_info["WORK_OF_ART"]:
                        reply += i
                        reply += " or "
                    reply = reply[:-4]
                    reply += '. You can call 000-000-0002 to get more information from local library.'
                    print(reply)
                    works = True
                #If there is any person inside the text, tell the user that I have no idea.
                if "PERSON" in ners_info:
                    reply = "You may want to find the person "
                    for i in ners_info["PERSON"]:
                        reply += i
                        reply += " or "
                    reply = reply[:-4]
                    if len(ners_info["PERSON"]) > 1:
                        reply += '. But I have no idea about them. Sorry about that.'
                    else:
                        reply += '. But I have no idea about he or she. Sorry about that.'
                    print(reply)
                    works = True
                

            #Do the sentiment analysis of the text
            ss = self.sentiment.polarity_scores(text)

            #If the text is positive, say some good words to the user.
            #If the text is negative, tell a joke to the user.
            if ss["pos"] >= 0.5:
                print("\nIt looks like you are pretty happy today. That\'s really good!")
                works = True
            elif ss["neg"] >= 0.5:
                print("\nIt looks like you are not very happy today. Let me tell you a joke: ")
                print("Mike: Mum, I want to watch TV.")
                print("Mum: There is no electricity tonight.")
                print("Then let\'s watch TV with a candie on.")
                print("Wish you happy.")
                works = True
            """
            for k in ss:
                print('{0}:{1},'.format(k, ss[k]))
            """
            #If all the above works cannot be done. Say sorry to the user.
            if not works:
                print("Sorry but I do not really understand what you said. Maybe I can help you with your next input.")
            text = input("Is there anything else I can help you? (input \'quit\' to leave concierge) ")



