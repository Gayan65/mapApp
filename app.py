from flask import Flask, render_template, request
from apis.api import get_direction

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    # To handle the error referenced before assignment
    json_data=None
    origin = None
    destination = None

    if request.method == 'POST':
        # Access form data from query parameters (GET method)
        origin = request.form.get('origin')
        destination = request.form.get('destination')
        json_data = get_direction(origin, destination)

    return render_template('index.html', data = json_data, origin = origin, destination = destination)

#css file route
@app.route('/styles/main.css')
def serve_css():
    return app.send_static_file('styles/main.css')


#favicon file route
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')


if __name__ == "__main__":
    app.run(debug=True)