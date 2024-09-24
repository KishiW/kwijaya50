# Kishi Wijaya
# TummyAKE
# SoftDev
# Title
# description

# 2024-09-20
# Time: start 10:33-10:59

'''
DISCO:
<note any discoveries you made here... no matter how small!>

QCC:
0. Java: Initilizing objects with parameters in the constructor
1. Path files / web links
2. The console
3. Prints name 
4. Doesn't appear anyways as it is not printed, just returned
5. Java - executing a pmethod with parameters that belong to a different class
 ...

INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''


from flask import Flask

app = Flask(__name__)                    # Q0: Where have you seen similar syntax in other langs?

@app.route("/")                          # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__)                      # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"             # Q4: Will this appear anywhere? How u know?

app.run()                                # Q5: Where have you seen similar constructs in other languages?



