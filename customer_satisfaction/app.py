from flask import Flask, render_template,url_for,request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/project')
def project():
    return render_template('project.html')

@app.route("/prediction",methods=['GET','POST'])
def prediction():
    if request.method == "POST":
        age = int(request.form['age'])
        flight_distance = int(request.form['flight_distance'])    
        infligth_entertainment = int(request.form["inflight-entertainment"])
        baggage_handling = int(request.form["baggage-handling"] )   
        cleanliness = int(request.form["cleanliness"])  
        departure_delay = int(request.form["departure_delay"])
        arrival_delay  = int(request.form["arrival_delay"])
        gender = int(request.form["gender"])
        customer_type  = int(request.form["customer-type"])
        travel_type = int(request.form["travel-type"])
        class_Type  = request.form["class-type"]

        UNSEEN_DATA = [age,flight_distance,infligth_entertainment,baggage_handling,
                       cleanliness,departure_delay ,arrival_delay,gender,
                       customer_type,travel_type,class_Type]
        return UNSEEN_DATA




if __name__ == "__main__":
    app.run(debug=True)