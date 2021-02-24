from data_cleaning import *
"""
split traning and testing data ration of 0.83 and 0.17 so 17% testing data to test model and 83% to train model
to convert words into number bcz computer only understands numbers (tokenizing)
"""

x_train,x_test,y_train,y_test=train_test_split(dataframe.clean_joined,dataframe.is_fake,test_size=0.17)
print(x_train)
print(y_train)

tokenizer=Tokenizer(num_words = ttl_wrds)

tokenizer.fit_on_texts(x_train)


train_tkns=tokenizer.texts_to_sequences(x_train)

test_tkns =tokenizer.texts_to_sequences(x_test)


print("The encoding for doc\n",dataframe.clean_joined[0],"\n is :",train_tkns[0])

padded_trn= pad_sequences(train_tkns ,maxlen=40 ,padding= "post" ,truncating="post")
padded_tst= pad_sequences(test_tkns ,maxlen=40,truncating="post")


for ind,doc in enumerate(padded_trn[:2]):
    print("The padded encoding for document",ind+1,"is : ",doc)
