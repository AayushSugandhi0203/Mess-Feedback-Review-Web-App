
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
import nltk
from collections import Counter
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer

#nltk.download()
example_sent = "This is a sample sentence, made make making showing made make making off the stop words filtration."

stop_words = set(stopwords.words('english')) 

word_tokens = word_tokenize(example_sent) 
word_tokens = [word for word in word_tokens if word.isalpha()]
filtered_sentence = [w for w in word_tokens if not w in stop_words] 

filtered_sentence = [] 

for w in word_tokens: 
	if w not in stop_words: 
		filtered_sentence.append(w) 
result = [item for items, c in Counter(filtered_sentence).most_common() 
                                      for item in [items] * c]   
new_list = []
print("Word Tokens", word_tokens) 
print("List Acc to freq",result) 
new_list = list(set(result))
print("Set of New List",new_list) 
remove_list = new_list.copy()
# Remove Participles 
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()


for i in new_list:
    a = lemmatizer.lemmatize(i)

    if a!=i and i in remove_list:
        remove_list.remove(i)
    lemmatizer.lemmatize(i,pos="a")
    
    if a!=i and i in remove_list:
        remove_list.remove(i)
    a = lemmatizer.lemmatize(i,'v')
    if a!=i and i in remove_list:
        remove_list.remove(i)    
        
print("Remove List",remove_list)

import tkinter as tk
from tkinter import *
import tkinter.messagebox as box
def dialog1():
    
    username = 4213
    if (username == '4213' ):
        box.showinfo('info','Correct Login')
    else:
        box.showinfo('info','Invalid Login')
window = Tk() 
window.title('Stop Words')

frame = Frame(window)
btn = Button(frame, text = result ,command = dialog1)
#btn = Button(frame, text = word_tokens,command = dialog1)
#btn = Button(frame, text = remove_list,command = dialog1)


btn.pack(side = RIGHT , padx =5)
frame.pack(padx=100,pady = 19)
window.mainloop()
