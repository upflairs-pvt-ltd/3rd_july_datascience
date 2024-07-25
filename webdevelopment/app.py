from flask import Flask,render_template
app = Flask(__name__)

@app.route('/')  # http://127.0.0.1:5000
def home():
    return render_template('home.html')

@app.route('/about')  # http://127.0.0.1:5000/about 
def about():
    return render_template('about.html')

@app.route('/service')  # http://127.0.0.1:5000/service
def service():
    return render_template('service.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)


