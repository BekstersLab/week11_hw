from flask import render_template, url_for, request, redirect
from application import app
# import datetime class from datetime module
from datetime import datetime
# import the get_time_slot function from utilities.py module
from application.utilities import get_time_slot

import mysql.connector

from FlaskWeek11_Bootstrap.application.utilities import get_portfolio_user, distinct_portfolio_user

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Pa$$w0rd",  # use for windows
    # password="",  # use for mac
    database="week11_hwk"
)

cursor = db.cursor()

# app.route decorator tells Flask what url should trigger the home_page() function
@app.route('/')
@app.route('/home')
def home_page():
    # get the current date and time
    time_now = datetime.now()
    # refers to get_time_slot function in utilites to determine time of day, (morning, afternoon or evening) based on hour returned
    time_slot = get_time_slot(time_now.hour)
    # '/' and '/home' urls trigger the 'home_page' function
    # app uses 'datetime' to get current time
    # get_time_slot function in utilities.py assigns time of day to a time slot (morning, afternoon, evening)
    # Jinja2 template dynamically generates html content (on home page)
    # uses time_slot variable in double braces to give a personalised greeting (on otherwise static home page)
    portfoliouser = distinct_portfolio_user()
    return render_template('home.html', title='Home', time_slot=time_slot, portfoliousers=portfoliouser)



@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


@app.route('/portfolio')
def portfolio_page():
    image_src_project_1 = url_for('static', filename='image/bek-images/PPC-News.png')
    external_url_project_1 = "https://github.com/BekstersLab/CFG-Web-Dev---Group-2/tree/main"
    image_src_project_2 = url_for('static', filename='image/bek-images/3-Column-Card.png')
    external_url_project_2 = "https://github.com/BekstersLab/3-column-preview-card-component-main/tree/main"
    image_src_project_3 = url_for('static', filename='image/bek-images/NFT-Preview-Card.png')
    external_url_project_3 = "https://github.com/BekstersLab/NFT-preview-card-component"
    return render_template('portfolio.html', title='Portfolio', image_src_project_1=image_src_project_1, external_url_project_1=external_url_project_1, image_src_project_2=image_src_project_2, external_url_project_2=external_url_project_2, image_src_project_3=image_src_project_3, external_url_project_3=external_url_project_3)


@app.route('/contact')
def contact_page():
    return render_template('contact.html', title='Contact')


@app.route('/contactcomplete')
def contact_complete():
    return render_template('contact_complete.html', title='Contact Complete')


# contact us form - posting the data input in the form to the db
@app.route('/contact', methods=['POST'])
def submit_contact_form():
        if request.method == 'POST':
            firstname = request.form['fname']
            lastname = request.form['lname']
            email = request.form['email']
            comments = request.form['comments']
            # checks if anything has been entered and populates a message if nothing entered
            if len(firstname) == 0 or len(lastname) == 0 or len(email) == 0 or len(comments) == 0:
                error = 'Please complete all fields'
                return render_template('contact.html', message=error)
            else:
                # Insert data into the users table
                sql = "INSERT INTO contact_information (firstname, lastname, email, comments) VALUES (%s, %s,%s, %s)"
                values = (firstname, lastname, email, comments)
                cursor.execute(sql, values)
                db.commit()
                # once done will redirect to completion page
                return redirect(url_for('contact_complete'))


# dynamic route for portfolio user using the value from the function
@app.route('/portfolio_dynamic/<portfoliouser>')
def user_portfolio(portfoliouser):
    portfolios = get_portfolio_user(portfoliouser)
    if not portfolios:
        return "Portfolio not found", 404
    print('Portfolios:', portfolios)
    try:
        return render_template('portfolio_dynamic.html', portfolios=portfolios)
    except Exception as e:
            print("Error rendering template:", e)
            # 500 is an internal server error http status code
            return "An error occurred while rendering the template", 500
