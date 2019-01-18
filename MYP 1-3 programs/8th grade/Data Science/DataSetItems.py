import statistics
print("Welcome to the data set finder, please begin inputting your data points and when you are done input end.")
done = False
dataset = []
while done == False:
    inputtedValue = input("Your data point, input 'end' if done:\n")
    if inputtedValue == "end":
        done = True
    else:
        dataset.append(int(inputtedValue))
print("Your data set is", dataset)
amount = 0
total = 0
for n in dataset:
    total+=n
    amount+=1
average = total/amount
print("The average is: {}".format(average))
print("The median is: {}".format(statistics.median(dataset)))
print("The range is: {}".format(max(dataset)-min(dataset)))
print("The mode is: {}".format(statistics.mode(dataset)))
