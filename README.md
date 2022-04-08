# Group-19

This repository is for our chat support bot. There are 4 main classes (returns, refund, test, main). Returns and refund classes are self-explanatory, as they contain the return and refund section respectively. The test class is a Q&A section for any questions the user may have. The main class is the main loop where all the code is combined. In order to run the code, spacy and nltk modules need to be installed. Then, run the "run_to_download_nltk.py" file. Finally, run the "main.py" file. (For return section, valid orderid is any integer 1-3).

Here's a complete list of changes that we made to our project following assignment 2.

Added an extra topic:
A new topic order_again is introduced. To use it, the users can type 'order again' just like they can type 'refund' or 'return' to use the other topics.
This topic is a process for the user to choose an ordered item and purchase it again, they can choose a payment method, choose a shipping facility, 
indicate the address and finally, choose the carrier. At the end of the chat, an order detail sheet will be presented to the user.

Use of other toolkits:
A new topic concierge is introduced to add some nlp functions for this project.
![image](https://user-images.githubusercontent.com/73769345/159101846-308d9392-741d-47ae-8a0d-44768d218370.png)

The spacy is used to do Tokenization, POS tagging and Tokenization.
The nltk is used to do sentiment analysis and Synonym recognition.

The user input text is tokenized by spacy and the tokens are saved. 

Tagging the pos of the tokens by spacy. 

Check if there is any noun inside the input text. 

Get the synonyms of all nouns by wordnet module of nltk.

If there are any synonyms of computer, phone or game, present the price list of the corresponding products.

Generate amed entity recognition of each token by spacy.

If there is any geo location inside the text, suggest the user to buy ticket.

If there is any art work inside the text, suggest the user to go to the library.

If there is any person inside the text, tell the user that I have no idea.

Do the sentiment analysis of the text by SentimentIntensityAnalyzer of nltk.

If the text is positive, say some good words to the user.

If the text is negative, tell a joke to the user.

If all the above items cannot be done. Say sorry to the user.

