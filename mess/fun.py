from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import os
vectorizer = CountVectorizer()

    
def prediction(str):    
    global vectorizer
    l = []
    l.append(str)
    #print(l)
    pkl_file = 'pickle_model.pkl'
    
    with open(pkl_file,'rb') as file:   
        model = pickle.load(file)
    
    print("52")
    #classifier = LogisticRegression()
    pkl_file_vectorizer = 'pickle_model_vectorizer.pkl'
    
    with open(pkl_file_vectorizer,'rb') as file:   
        vectorizer = pickle.load(file)
    
    lots  = vectorizer.transform(["I really enjoyed my visit here "])
    pred = model.predict(lots)
    return pred
    

def training():
    filepath_dict = {
        'funs':   'C:/Users/TCD/Desktop/Python/train.csv',

    }
    filepath_dict_test = {

        'testfuns':    'C:/Users/TCD/Desktop/Python/data_test1.csv'
    }
    df_list = []
    train = pd.read_csv('train.csv')
    data_test1 = pd.read_csv('data_test1.csv')

    train.drop(["cool", "date", "review_id", "stars",
            "useful", "user_id"], axis=1, inplace=True)
    data_test1.drop(["cool", "date", "review_id", "stars",
                 "useful", "user_id"], axis=1, inplace=True)

    df_list.append(train)
    df_list_test = []

    df_list_test.append(data_test1)

    df = pd.concat(df_list)
    df_text = list(df['text'])

    y = list(df['funny'])


    df_test = pd.concat(df_list_test)

    df_text_test = list(df_test['text'])
    #print(len(df_text_test))

    y_test = list(df_test['funny'])
    
    df_train, df_test, y_train, y_test = train_test_split(
        df_text, y, test_size=0.25, random_state=1000)


# Split data
    global vectorizer
    vectorizer = CountVectorizer()
    vectorizer.fit(df_train)

    X_train = vectorizer.transform(df_train)

    X_test = vectorizer.transform(df_test)

    lol = vectorizer.transform(df_text_test)



    classifier = LogisticRegression()
    classifier.fit(X_train, y_train)


    predict = classifier.predict(X_test)

    score = classifier.score(X_test, y_test)
    report = classification_report(y_test, predict)



    confuse = confusion_matrix(y_test, predict)
    print(confuse)
    filename = 'pickle_model.pkl'
    with open(filename,'wb') as file:
        pickle.dump(classifier,file)
        
    filename = 'pickle_model_vectorizer.pkl'
    with open(filename,'wb') as file:
        pickle.dump(vectorizer,file)    
    str = "I love her very much but she rejeceed me." 
    y = prediction(str)
    
    print(y)
    

if __name__=="__main__":
    training()
    # str = "I love her very much but she rejeceed me." 
    # y = prediction(str)
    # print(y)