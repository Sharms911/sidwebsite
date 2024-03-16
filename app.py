from flask import Flask, render_template

app = Flask(__name__)
app.config['STATIC_URL_PATH'] = '/sidwebsite/static'

@app.route('/sidwebsite/')
def index():
    return render_template('index.html')

@app.route('/sidwebsite/contact')
def contact():
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
