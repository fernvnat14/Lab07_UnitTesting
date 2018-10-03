import sqlite3
conn = sqlite3.connect('Users.db')
c = conn.cursor()

# Input username and password to check validation
username = input('Input username:  ')
password = input('Input password:  ')

# Create function to check if username and password are match
def check_login(username, password):
    valid_check = c.execute("SELECT COUNT(*) AS NUM FROM Users WHERE username = (?) AND password = (?)",
                      [(username),(password)])
    for value in valid_check:
        check = value[0]
        if check == 1:
            print('Passed')
            return 'Passed'
        else:
            username_check = c.execute("SELECT * FROM Users WHERE username = (?)" ,
                               [(username)])  # Check password from username
            for value2 in username_check:
                c_pass = value2[1]
                if str(password) != str(c_pass) :
                    print('Incorrect password')
                    return 'Incorrect password'
