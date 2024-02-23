from flask import Flask, render_template, request
from apis.api import get_direction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        # Access form data from query parameters (GET method)
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        print(origin, destination)
        get_direction(origin, destination)

    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)