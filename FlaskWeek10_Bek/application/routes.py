from flask import render_template, url_for, request, redirect
from application import app
from datetime import datetime
from application.utilities import get_time_slot

import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="Pa$$w0rd",  # use for windows
    password="",  # use for mac
    database="week11_hwk"
)

cursor = db.cursor()


# a get route by default, unless specified otherwise
@app.route('/')  # decorator that tells Flask which URL should trigger the function below
@app.route('/home')  # can have more than one decorator allowing function to be accessible from different url
def home_page():  # define function called when root or /home url is accessed
    # 'url_for()' dynamically builds urls for specific functions
    # takes name of function you want to generate an url for as an argument
    # avoids hard coding urls so if route is changed the urls don't need manually updating throughout app
    # 'url_for()' automatically generates correct url based on new route
    home_url = url_for('home_page')  # 'url_for()' dynamically generates url for home_page and stores in a variable
    about_url = url_for('about_page')  # generates url for about page
    portfolio_url = url_for('portfolio_page')  # generates url for portfolio page
    contact_url = url_for('contact_page')  # generates url for contact page
    # within this function, 'home_url = url_for('home_page')' generates an url path for the home_page function and ...
    # assigns it to the home_url variable. The url path corresponds to '@app.route('/')' or '@app.route(/home)' decorator
    # the variables are used to create hyperlinks (<a></a>) within the navigation section of each page
    # e.g. '{home_url}' is replaced with the generated url for the home page when Python code is executed

    time_now = datetime.now()
    time_slot = get_time_slot(time_now.hour)
    return render_template('home.html', title='Home', time_slot=time_slot, home_url=home_url, about_url=about_url, portfolio_url=portfolio_url, contact_url=contact_url)


# structure is similar for about_page
# the decorator tells Flask the about url should trigger the function below
@app.route('/about')
def about_page():  # define the function for the about page
    home_url = url_for('home_page')  # identical to code in home_page function
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return render_template('about.html', title='About', home_url=home_url, about_url=about_url, portfolio_url=portfolio_url, contact_url=contact_url)


# repeat the structure for contact_page
@app.route('/contact')
def contact_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return render_template('contact.html', title='Contact', home_url=home_url, about_url=about_url, portfolio_url=portfolio_url, contact_url=contact_url)


@app.route('/contactcomplete')
def contact_complete():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    return render_template('contact_complete.html', title='Contact Complete', home_url=home_url, about_url=about_url, portfolio_url=portfolio_url, contact_url=contact_url)


@app.route('/contact', methods=['POST'])
def submit_contact_form():
        if request.method == 'POST':
            firstname = request.form['fname']
            lastname = request.form['lname']
            email = request.form['email']
            comments = request.form['comments']

            # Insert data into the users table
            sql = "INSERT INTO contact_information (firstname, lastname, email, comments) VALUES (%s, %s,%s, %s)"
            values = (firstname, lastname, email, comments)

            cursor.execute(sql, values)
            db.commit()

            return redirect(url_for('contact_complete'))

        return 'Invalid request'


# repeat the structure for portfolio_page
# addition of variables for image sources and external urls to link to
@app.route('/portfolio')
def portfolio_page():
    home_url = url_for('home_page')
    about_url = url_for('about_page')
    portfolio_url = url_for('portfolio_page')
    contact_url = url_for('contact_page')
    image_src_project_1 = url_for('static', filename='Image/PPC-News.png')
    external_url_project_1 = "https://github.com/BekstersLab/CFG-Web-Dev---Group-2/tree/main"
    image_src_project_2 = url_for('static', filename='Image/3-Column-Card.png')
    external_url_project_2 = "https://github.com/BekstersLab/3-column-preview-card-component-main/tree/main"
    image_src_project_3 = url_for('static', filename='Image/NFT-Preview-Card.png')
    external_url_project_3 = "https://github.com/BekstersLab/NFT-preview-card-component"
    return render_template('portfolio.html', title='Portfolio', home_url=home_url, about_url=about_url, portfolio_url=portfolio_url, contact_url=contact_url, image_src_project_1=image_src_project_1, external_url_project_1=external_url_project_1, image_src_project_2=image_src_project_2, external_url_project_2=external_url_project_2, image_src_project_3=image_src_project_3, external_url_project_3=external_url_project_3)







