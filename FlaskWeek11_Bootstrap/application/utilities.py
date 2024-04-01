import mysql.connector


def get_time_slot(time):
    if time < 12:
        return "morning"
    elif time < 18:
        return "afternoon"
    else:
        return "evening"


# Function to get the data for each portfolio row for a user in the portfolio db
def get_portfolio_user(portfoliouser):
    # connect to the database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # use for windows
        # password="",  # use for mac
        database="week11_hwk"
    )
    # flask interacting with mysql db
    # returns the data from a query into a list of dictionary's
    cursor = connection.cursor(dictionary=True)
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

