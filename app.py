from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'GET':
        # Access form data from query parameters (GET method)
        origin = request.args.get('origin')
        destination = request.args.get('destination')
        print(origin, destination)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)