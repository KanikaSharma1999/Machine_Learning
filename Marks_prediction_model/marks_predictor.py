import joblib
mind=joblib.load("mymarkspredict.model")
h=int(input("Enter your hours of study :"))
fscore=mind.predict([[h]])
print(fscore)