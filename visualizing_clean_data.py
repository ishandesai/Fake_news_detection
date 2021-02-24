"""countplot for individual numbers of subject to subject (bar graph)
plot which words are frequently used in true news and fake news
maximum numbers of words in a data in data frame(maximum_len)

"""
from data_cleaning import *




plot.figure(figsize=(10,10))
sns.countplot(y="subject",data=dataframe)
plot.show()
plot.figure(figsize=(20,20))


wrd_cld=WordCloud(max_words=2000,width=1600,height=800,stopwords=stp_wrd).generate(" ".join(dataframe[dataframe.is_fake==1].clean_joined))

plot.imshow(wrd_cld,interpolation='bilinear')
plot.show()
wrd_cld=WordCloud(max_words=2000,width=1600,height=800,stopwords=stp_wrd).generate(" ".join(dataframe[dataframe.is_fake==0].clean_joined))

plot.imshow(wrd_cld, interpolation='bilinear')
plot.show()

maximum_len= - 2**35
for doc in dataframe.clean_joined:
    tkns=nltk.word_tokenize(doc)
    if(maximum_len<len(tkns)):
        maximum_len=len(tkns)
print("The maximum numbers of words in dataframe is=",maximum_len)


figure= pltexp.histogram( x= [len(nltk.word_tokenize(x)) for x in dataframe.clean_joined], nbins= 100 )
figure.show()
