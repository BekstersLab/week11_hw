import mysql.connector

git 
# define function to determine morning, afternoon or evening based on current time (hour)
def get_time_slot(time):
    if time < 12:
        return "morning"
    elif time < 18:
        return "afternoon"
    else:
        return "evening"


def get_db_connection():
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # use for windows
        # password="",  # use for mac
        database="week11_hwk"
    )
    return connection


# Function to get the data for each portfolio row for a user in the portfolio db
def get_portfolio_user(portfoliouser):
    # connection to the database in the function above
    conn = get_db_connection()
    # flask interacting with mysql db
    # returns the data from a query into a list of dictionary's
    cursor = conn.cursor(dictionary=True)
    sql = """
    SELECT Portfoliouser, 
    imagelink, 
    Projectheader, 
    Projectparagraph1, 
    Projectparagraph2, 
    Projectparagraph3, 
    Projectparagraph4, 
    Projectlink
    FROM portfolio
    WHERE portfoliouser = %s
    """
    cursor.execute(sql, (portfoliouser,))
    # fetches all the rows
    result_set = cursor.fetchall()
    return result_set

print(get_portfolio_user('katy'))


def distinct_portfolio_user():
    conn = get_db_connection()
    cursor = conn.cursor()
    # gets the distinct rows from the db
    cursor.execute("SELECT DISTINCT Portfoliouser FROM portfolio")
    # iterates over the rows to get the first column of each row
    portfoliousers = [row[0] for row in cursor.fetchall()]
    # turns the output into a string which can then be populated
    portfolioruser_str = portfoliousers[0]
    return portfolioruser_str
