from flask import Flask, render_template, request
from database import get_all_hotels, create_hotel, get_one_hotel
app = Flask(__name__)


@app.route('/')
def home():
	hotels = get_all_hotels()
	return render_template("home.html", hotels=hotels)


@app.route('/create', methods =["GET","POST"])
def hotel():
	if request.method =="GET":
		return render_template('form.html')
	else:
		name = request.form['name']
		booking_date = request.form['booking_date']
		description = request.form['description']
		price = request.form['price']
		photo = request.form['photo']
		create_hotel(name, booking_date, description, price, photo)
		hotel = get_all_hotels()
		return render_template('home.html', hotel = hotel)

@app.route('/<int:id>')
def page_hotel(id):
    hotel = get_one_hotel(id)
    return render_template("hotel.html",hotel = hotel)

if __name__ == '__main__':
    app.run(debug=True)

