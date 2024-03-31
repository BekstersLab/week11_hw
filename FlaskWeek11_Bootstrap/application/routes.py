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


@app.route('/')
@app.route('/home')
def home_page():
    time_now = datetime.now()
    time_slot = get_time_slot(time_now.hour)
    return render_template('home.html', title='Home', time_slot=time_slot)


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
