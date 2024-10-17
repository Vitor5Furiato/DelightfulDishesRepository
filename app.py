from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'delightfuldishes'
mysql = MySQL(app)
@app.route('/maintenance')
def maintenance():
    return render_template('maintenance.html')

@app.route('/input_user')
def input_user():
    return render_template('input_user.html')

@app.route('/add_user', methods=['POST'])
def add_user():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO User (username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cursor.close()
        
        return render_template('feedback.html', message="User added successfully!")
    else:
        return redirect(url_for('input_user'))


@app.route('/input_recipe')
def input_recipe():
    return render_template('input_recipe.html')

@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    if request.method == 'POST':
        recipe_name = request.form['recipe_name']
        instructions = request.form['instructions']
        recipe_type = request.form['type']
        rating = request.form['rating']
        
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Recipe (recipeName, instructions, type, rating) VALUES (%s, %s, %s, %s)",
                       (recipe_name, instructions, recipe_type, rating))
        mysql.connection.commit()
        cursor.close()
        
        return render_template('feedback.html', message="Recipe added successfully!")
    else:
        return redirect(url_for('input_recipe'))

@app.route('/input_favorites')
def input_favorites():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT userID, username FROM User")
    users = cursor.fetchall()
    cursor.execute("SELECT recipeID, recipeName FROM Recipe")
    recipes = cursor.fetchall()
    cursor.close()
    
    return render_template('input_favorites.html', users=users, recipes=recipes)

@app.route('/add_favorite', methods=['POST'])
def add_favorite():
    if request.method == 'POST':
        user_id = request.form['userID']
        recipe_id = request.form['recipeID']
        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO Favorites (userID, recipeID) VALUES (%s, %s)", (user_id, recipe_id))
        mysql.connection.commit()
        cursor.close()
        
        return render_template('feedback.html', message="Favorite added successfully!")
    else:
        return redirect(url_for('input_favorites'))

if __name__ == '__main__':
    app.run(debug=True)
