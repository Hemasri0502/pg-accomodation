from flask import Flask, render_template, request
from templates.priority_1 import *
#from templates.db_code import PGASDB
app = Flask(__name__)
app.debug = True

@app.route('/')
def home():
    
    return render_template('getlocation.html')

@app.route('/home', methods=['GET','POST'])
def get_input():
    location = request.form.get("location")

    target_latitude,target_longitude= get_lat_lng(location)
    print(target_latitude)

    pgasdb = PGASDB('localhost', 'root', '', 'pgasdb')
    output_records = pgasdb.calculate_distance(target_latitude, target_longitude)
    pgasdb.close_connection()
    h=heap()
    for i in output_records:
        res=h.insert(i)
        print("hiiiiii",res[1][2])
    h2=heap()
    for i in output_records:
        res_budget=h2.insert_budget(i)
    return render_template('display.html',distance_accomodation =res[1][2],budget_accomodation=res_budget[1][3])

@app.route('/home/booking', methods=['GET','POST'])
def booking():
    
    return render_template('booking.html')

@app.route('/home/booking/afterbooking', methods=['GET','POST'])
def afterbook():
    
    return render_template('afterbook.html')

@app.route('/home/about')
def about():
    
    return render_template('about.html')
@app.route('/home/booking/afterbooking/about/contact')
def contact():
    
    return render_template('contact.html')
@app.route('/home/booking/afterbooking/about/contact/login')
def login():
    return render_template("login.html")


   

        

if __name__ == '__main__':
    app.run()

        