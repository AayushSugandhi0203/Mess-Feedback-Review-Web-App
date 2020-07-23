from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
import pandas as pd
import itertools
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import pickle
import os
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
vectorizer = CountVectorizer()

def prediction(str):
    global vectorizer
    l = []
    l.append(str)
    #print(l)
    pkl_file = 'pickle_model_classify.pkl'
    pkl_file =os.path.dirname(__file__) + "/" + pkl_file
    with open(pkl_file,'rb') as file:   
        model = pickle.load(file)
    
    print("52")
    
    #classifier = LogisticRegression()
    pkl_file_vectorizer = 'pickle_model_vectorizer_classify.pkl'
    pkl_file_vectorizer =os.path.dirname(__file__) + "/" + pkl_file_vectorizer
    with open(pkl_file_vectorizer,'rb') as file:   
        vectorizer = pickle.load(file)
    lot = vectorizer.transform(l)
    
    predict_string = model.predict(lot)
    print(predict_string)
    return predict_string
    
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

    train.drop(["cool", "date", "review_id", "funny",
                "useful", "user_id"], axis=1, inplace=True)
    data_test1.drop(["cool", "date", "review_id", "funny",
                    "useful", "user_id"], axis=1, inplace=True)

    df_list.append(train)
    df_list_test = []

    df_list_test.append(data_test1)


    df = pd.concat(df_list)
    df_text = list(df['text'])

    y = list(df['stars'])

    df_test = pd.concat(df_list_test)

    df_text_test = list(df_test['text'])


    y_test = list(df_test['stars'])
    df_train, df_test, y_train, y_test = train_test_split(
        df_text, y, test_size=0.25, random_state=1000)

    vectorizer = CountVectorizer()
    vectorizer.fit(df_train)

    X_train = vectorizer.transform(df_train)

    X_test = vectorizer.transform(df_test)



    lol = vectorizer.transform(df_text_test)



    model = LogisticRegression(solver = 'saga')
    model.fit(X_train, y_train)
    # use the model to make predictions with the test data
    y_pred = model.predict(X_test)
    # how did our model perform?
    print(y_pred)

    accuracy = metrics.accuracy_score(y_test, y_pred)
    #print('Accuracy: {:.2f}'.format(accuracy))

    data_pred = model.predict(lol)
    print(data_pred)
    filename = 'pickle_model_classify.pkl'
    with open(filename,'wb') as file:
        pickle.dump(model,file)
        
    filename = 'pickle_model_vectorizer_classify.pkl'
    with open(filename,'wb') as file:
        pickle.dump(vectorizer,file)    
    str = "I love her very much but she rejeceed me." 
    y = prediction(str)
    
    print(y)

if __name__=="__main__":
    #training()
    str = "I love her very much but she rejeceed me." 
    y = prediction(str)
    print(y)
    
 
