
from flask import Flask, render_template, request, session
# import bcrypt
# import ibm_db
# conn = ibm_db.connect("DATABASE=buldb;HOSTNAME=21fecfd8-47b7-4937-840d-d791d0218660.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=31864;USERNAME=kdp42382;PASSWORD=0Bs2TiQqFLOkp9nQ;SECURITY=SSL;SSLSERVERCERTIFICATE=DigiCertGlobalRootCA.crt;", "", "")
app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    # if 'email' not in session:
    return render_template('home.html', name='Home')


@app.route("/home", methods=['GET', 'POST'])
def signup():
    #   if request.method == 'POST':
    #     email = request.form['Email Address']
    #     password = request.form['Password']
    #     password = request.form['Confirm Password']
    #     if not email or not password:
    #         return render_template('home.html')
    #     hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    #     query = "SELECT * FROM USERS WHERE email=? OR password=?"
    #     stmt = ibm_db.prepare(conn, query)
    #     ibm_db.bind_param(stmt, 1, email)
    #     ibm_db.bind_param(stmt, 2, password)
    #     ibm_db.execute(stmt)
    #     isUser = ibm_db.fetch_assoc(stmt)

    #     if not isUser:
    #         insert_sql = "INSERT INTO User(,email,PASSWORD,) VALUES (?,?,)"
    #         prep_stmt = ibm_db.prepare(conn, insert_sql)
    #         ibm_db.bind_param(prep_stmt, 1, email)
    #         ibm_db.bind_param(prep_stmt, 2, password)
    #         ibm_db.execute(prep_stmt)
    return render_template('editportfolio.html')

# @app.route("/home",methods=['GET','POST'])
# def login():
#     if request.method == 'POST':
#         email = request.form['email']
#         password = request.form['password']


#         if not email or not password:
#             return render_template('home.html')
#         query = "SELECT * FROM USERS WHERE email=?"
#         stmt = ibm_db.prepare(conn, query)
#         ibm_db.bind_param(stmt, 1, email)
#         ibm_db.execute(stmt)
#         isUsers = ibm_db.fetch_assoc(stmt)
#         print(isUsers, password)
#         if not isUsers:
#            return render_template('home.html')
#         isPasswordMatch = bcrypt.checkpw(password.encode('utf-8'), isUsers['PASSWORD'].encode('utf-8'))
#         if not isPasswordMatch:
#            return render_template('home.html')
#         session['email'] = isUsers['EMAIL']

#         return render_template('home.html')


if __name__ == '__main__':
    app.run()
