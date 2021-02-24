from data_tkn_pdg import *
"""
build machine learning model for fake_news_model detection using Google's tensorflow
add some neural to make it dense for more accuracy
and train it for 3 epochs so accuracy loss would be minimum
"""
fake_news_model=Sequential()

fake_news_model.add(Embedding(ttl_wrds,output_dim=240))

fake_news_model.add(Bidirectional(LSTM(240)))

fake_news_model.add(Dense(240,activation="relu"))




fake_news_model.add(Dense(1,activation="sigmoid"))

fake_news_model.compile(optimizer="adam",loss="binary_crossentropy",metrics=['acc'])

fake_news_model.summary()

print(ttl_wrds)

y_train=np.asarray(y_train)

fake_news_model.fit(padded_trn,y_train,batch_size = 64,validation_split=0.15,epochs=3)
