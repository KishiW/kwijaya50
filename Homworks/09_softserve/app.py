#Victor Casado
#The Strawberry Pickers
#SoftDev
#K09 -- Putting occupations on a website
#2024-09-23
#time spent:
import random as r
def pickrand():
    f = open("occupations.csv", "r")
    string = f.read()

    list = string.split("\n")
    list = list[1:len(list)-2] #removes example row, total row, and new line row

    names = []
    nums = []
#counter = 0

    for i in range(len(list)):
        if(list[i][0] == "\""):
            indexcomma = list[i][1:].index("\"") + 2
            name = list[i][1:indexcomma - 1] #starts at first quote, ends at second quote
            num = list[i][indexcomma + 1:]
        else:
            split = list[i].split(",")
            name = split[0]
            num = split[1]
        names.append(name)
        nums.append(float(num))
    #counter += 1
    #print(str(counter) + ": " + name)
#print(names)
#print(nums)
#print(dict)
    return r.choices(names, nums)[0]




from flask import Flask
app = Flask(__name__)           #create instance of class Flask

@app.route("/")                 #assign fxn to route
def hello_world():
    return pickrand()

if __name__ == "__main__":      # true if this file NOT imported
    app.debug = True            # enable auto-reload upon code change
    app.run()
