import mysql.connector


def get_time_slot(time):
    if time < 12:
        return "morning"
    elif time < 18:
        return "afternoon"
    else:
        return "evening"


# Function to get team member and their projects from MySQL
def get_portfolio_user(portfoliouser):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Pa$$w0rd",  # use for windows
        # password="",  # use for mac
        database="week11_hwk"
    )
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
    result_set = cursor.fetchall()
    return result_set

print(get_portfolio_user('katy'))

