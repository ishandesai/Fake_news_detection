from data_analysis import *
"""
to remove some  unnecessary words like use,it,my etc which is in stopwords.words and has len of 3 or less than 3
make another column in which all stopwords are removed (clean column )and concatenate all words into one large string in new column clean_joined
"""

stp_wrd = stopwords.words('english')

stp_wrd.extend(['from', 'subject', 're', 'edu', 'use'])


def preprocessing(string):
    result = []
    for tkn in gensim.utils.simple_preprocess(string):
        if tkn not in gensim.parsing.preprocessing.STOPWORDS and len(tkn) > 3 and tkn not in stp_wrd:
            result.append(tkn)
    return result


dataframe['clean'] = dataframe['original'].apply(preprocessing)

print(dataframe['original'][0])

print(dataframe['clean'][0])

print(dataframe)

wrds = []

for dtls in dataframe.clean:
    for dtl in dtls:
        wrds.append(dtl)
print(wrds)

print(len(wrds))

ttl_wrds = len(list(set(wrds)))

dataframe['clean_joined'] = dataframe['clean'].apply(lambda x: " ".join(x))

print(dataframe)

print(dataframe['clean_joined'][0])
