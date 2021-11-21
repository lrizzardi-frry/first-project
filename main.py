# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def show_index():
    return render_template('primeiroTesteEmHTML.html')


def print_hi():
    name = input("Hey, qual o seu nome? ")
    # Use a breakpoint in the code line below to debug your script.
    print(f'Olá, {name}! Seja bem-vindo ao meu primeiro projeto!')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run('localhost', 8000)
