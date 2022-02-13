# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from flask import Flask
from flask import app
import flask

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

app = Flask (__name__)
@app.route('/')
def hello():
    return "hello"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
