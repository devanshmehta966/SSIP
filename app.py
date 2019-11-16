import pymysql
from flask import Flask, request, render_template,redirect


app = Flask(__name__)


@app.route('/')
def loadPage():
    return render_template('JobPortol.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='root',
        db='db_python'
    )
    if request.method == 'POST':
        a = request.form['f_name']
        b = request.form['l_name']
        c = request.form['u_name']
        d = request.form['pwd']
        e = request.form['repwd']

        cursor1 = connection.cursor()

        cursor1.execute(
            "INSERT INTO jobportolreg(FirstName,LastName,UserName,NewPassword,RePassword) VALUES ('" + a + "','" + b + "','" + c + "','" + d + "','" + e + "')")

        connection.commit()

        cursor1.close()

        connection.close()

        return redirect('JobPortol.html',code=304)#compulsary for app.route

# @app.route('/Login', methods=["post"])
# def signIn():
#
#     connection = pymysql.connect(
#         host='localhost',
#         user='root',
#         password='root',
#         db='db_python')
#
#     if request.form["u_name"] != "" and request.form["pwd"] != "":
#         un = request.form["u_name"]
#         pwd = request.form["pwd"]
#
#         sql_select_Query = "select u_name,pwd from jobportolreg"
#         cursor = connection.cursor()
#         cursor.execute(sql_select_Query)
#         records = cursor.fetchall()
#






if __name__ == "__main__":
    app.debug=True
    app.run()

