import configparser
import mysql.connector

config = configparser.ConfigParser()
config.read('config.ini')

host = config['db_credentials']['host']
name = config['db_credentials']['name']
user = config['db_credentials']['user']
password = config['db_credentials']['password']

print(f"   HERE I AM {host}")
print(f"   HERE I AM {password}")

from flask import Flask, render_template

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    # Connect to MySQL Database
    conn = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=name,
        port=3306
    )
    
    # Execute SQL Query to Fetch Data from TABLE 5
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM `TABLE 5`')
    rows = cursor.fetchall()
    
    # Close Database Connection
    cursor.close()
    conn.close()
    
    # Render HTML Template and Pass Data
    return render_template('index.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)


