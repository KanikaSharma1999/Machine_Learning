import joblib
mind=joblib.load("predictmarks.model")
hrs=input('Enter the no. of hours of study:-')
finalmarks=mind.predict([[int(hrs)]])
print("Your final marks are:",finalmarks)