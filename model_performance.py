from build_train_model import *
"""
measure accuracy of our model using testing data from earlier (17 % of total dataset)
and plot confusion_matrix to know how much data from dataset is unclassified
"""
predict= fake_news_model.predict(padded_tst)

predict_lst=[]

for ind in range(len(predict)):
    if predict[ind].item() >0.5:
        predict_lst.append(1)
    else:
        predict_lst.append(0)

acc= accuracy_score(list(y_test),predict_lst)

print("Fake news model accuracy:",acc)

cm =confusion_matrix(list(y_test),predict_lst)

plot.figure(figsize=(25,25))
sns.heatmap(cm,annot=True)
plot.show()
