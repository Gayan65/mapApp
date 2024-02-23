from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'GET':
        # Access form data from query parameters (GET method)
        name = request.args.get('name')
        print(name)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)