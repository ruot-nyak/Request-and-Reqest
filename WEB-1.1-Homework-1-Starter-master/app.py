from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    """Shows a greeting to the user."""
    return 'Are you there, world? It\'s me, Ducky!'

@app.route('/animal/<users_animal>')
def favorite_animal(users_animal):
    """Display a message to the user that changes based on their favorite animal."""
    return f'Wow, {users_animal} is my favorite animal, too!'

@app.route('/dessert/<users_dessert>')
def favorite_dessert(users_dessert):
    return f'How did you know I liked {users_dessert}'

@app.route('/madlibs/<adjective>/<noun>')
def mad_libs(adjective, noun):
    return f'The man walked up and saw a, {adjective} {noun}.'

@app.route("/multiply/<num1>/<num2>")
def multiply(num1,num2)
    if (num1.isdigit() == True) (num2.isdigit() == True)
        solution = int(num1) * int(num2)
        return solution
    else:
        return "Invalid inputs. Please try again by entering 2 numbers!"

if __name__ == '__main__':
    app.run(debug=True)
