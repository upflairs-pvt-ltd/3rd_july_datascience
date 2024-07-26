from flask import Flask,render_template,url_for,request
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

@app.route('/query')   #http://127.0.0.1:5000/query
def query():
    return render_template('query.html')


@app.route('/user_query',methods=['GET','POST'])
def user_query():
    if request.method == "POST": 
        name = request.form['name']
        age = request.form['age']
        address = request.form['address']
        college = request.form['college']
        branch = request.form['branch']
        roll_no = request.form['roll_no']
        query_sub = request.form['query_sub']

        user_data = [name,age,address,college,branch,roll_no,query_sub]
        return user_data 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)


