import googletrans
import time
from googletrans import Translator

def trans():
    check = True
    while check == True:
        translator = Translator()
        time.sleep(1)
        phrase = str(input("What phrase would you like to translate?"))
        original = translator.detect(phrase).lang
        time.sleep(1.5)
        print("The detected language is:", googletrans.LANGUAGES[original])
        time.sleep(1)
        print("Here is a list of languages that you will be able to translate to: \n", googletrans.LANGUAGES)
        time.sleep(2)
        print("Notice there are codes for each language, you will be asked to input a code for the translation.")
        time.sleep(2)
        new = str(input("What language would you like to translate the phrase to?"))
        time.sleep(1)
        translation = translator.translate(phrase, src=original, dest=new)
        time.sleep(1)
        print("Phrase entered:", phrase)
        time.sleep(.5)
        print("Phrase Language:", googletrans.LANGUAGES[original])
        time.sleep(.5)
        print("Translated Phrase:", translation.text)
        time.sleep(.5)
        print("Translated Language:", googletrans.LANGUAGES[new])
        response = str(input("Would you like to translate another phrase? (y/n)"))
        if response.lower() == 'n':
            check = False
        else:
            continue

if __name__ == '__main__':
    trans()

