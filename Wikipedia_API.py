import wikipediaapi
import time

def search():
    check = True
    while check == True:
        wiki = wikipediaapi.Wikipedia('en')
        time.sleep(1)
        response = str(input("What would you like to learn about?"))
        page = wiki.page(response.replace(' ', '_'))
        time.sleep(1.5)
        print("Page - Title:", page.title)
        time.sleep(1.5)
        print("Page - Summary:", page.summary)
        time.sleep(1.5)
        response2 = str(input("Would you like to learn about another topic? (y/n)"))
        if response2.lower() == 'n':
            check = False
        else:
            continue


if __name__ == '__main__':
    search()