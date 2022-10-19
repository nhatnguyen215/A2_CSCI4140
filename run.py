from flask import Flask, render_template, request, flash
from flask_mysqldb import MySQL
import random, datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'admin'
app.config['MYSQL_DB'] = 'mydb'
 
mysql = MySQL(app)

# set as part of the config
SECRET_KEY = 'many random bytes'

# or set directly on the app
app.secret_key = 'many random bytes'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/parts', methods=['GET', 'POST'])
def parts():
    try:
        cur = mysql.connection.cursor()
        cur.execute('''SELECT * FROM mydb.parts207''')
        data = cur.fetchall()
        cur.close()
        return render_template("parts.html", data=data)
    except Exception as e:
        return str(e)

@app.route('/po', methods=['GET', 'POST'])
def po():
    #SELECT list of clients
    cur = mysql.connection.cursor()
    cur.execute('''SELECT clientId207 FROM mydb.clients207''')
    clientIDList = cur.fetchall()
    print(clientIDList)
    cur.close()

    #SELECT list of part numbers
    cur = mysql.connection.cursor()
    cur.execute('''SELECT partNo007 FROM mydb.parts207''')
    partNoList = cur.fetchall()
    cur.close()

    if request.method == 'POST':
        compID = request.form['compID']
        clientID = request.form['clientID']
        partNo = request.form['partNo']
        qty = request.form['qty']
        poNo = random.randint(100,1000)
        status = 'Pending'
        date = datetime.date.today()

        #Check if clientID entered matches the ones in the system
        clientIDCheck = False
        for i in clientIDList:
            for j in i:
                if int(clientID) == int(j):
                    clientIDCheck = True 
        print('clientidcheck', clientIDCheck)
        #Check if the partNo entered matches the ones in the system
        partNoCheck = False
        for i in partNoList:
            for j in i:
                if int(partNo) == int(j):
                    partNoCheck = True
        print('Part no check', partNoCheck)
        #Query to find qoh of a part
        cur = mysql.connection.cursor()
        qohQuery = '''SELECT qoh207 FROM mydb.parts207 WHERE partNo007 = %s'''
        cur.execute(qohQuery, partNo)
        qohList = cur.fetchall()
        cur.close()

        #Check if qoh is less than quantity ordered or no
        qohCheck = False
        for i in qohList:
            for j in i:
                if int(qty) < int(j):
                    qohCheck = True
        print('qoh check', qohCheck)
        
        if clientIDCheck == True and qohCheck == True and partNoCheck == True:
            #Insert PO 
            poQuery ="""INSERT INTO mydb.pos207 (poNo207, clientCompID207, dataOfPO207,status207, Clients207_clientId207)
                    VALUES (%s, %s, %s, %s, %s)"""
            poValues = (poNo, compID, date, status, clientID)
            cur = mysql.connection.cursor()
            cur.execute(poQuery, poValues)
            mysql.connection.commit()
            cur.close()

            #Query to find price of entered part
            cur = mysql.connection.cursor()
            priceQuery = '''SELECT currentPrice207 FROM mydb.parts207 WHERE partNo007 = %s'''
            cur.execute(priceQuery, partNo)
            priceList = cur.fetchall()
            cur.close()

            price = 0
            for i in priceList:
                for j in i:
                    price = j

            #Insert line
            lineQuery ="""INSERT INTO mydb.lines207 (POs207_poNo207, Parts207_partNo007, qty207, priceOrdered207)
                    VALUES ( %s, %s, %s, %s)"""
            lineValues = (poNo, partNo, qty, price)
            cur = mysql.connection.cursor()
            cur.execute(lineQuery, lineValues)
            mysql.connection.commit()
            cur.close()
        else:   
            return render_template('inputError.html')


    return render_template('po.html')

@app.route('/poList', methods=['GET', 'POST'])
def poList():
    globalData = ''
    if request.method == "POST":
        clientID = request.form.get('clientID')
        cur = mysql.connection.cursor()
        query = """SELECT * FROM mydb.pos207 WHERE Clients207_clientId207 = %s"""
        cur.execute(query, [clientID])
        data = cur.fetchall()
        globalData = data
        cur.close()
        
    return render_template('poList.html', data=globalData) 

@app.route('/line', methods=['GET', 'POST'])
def line():
    globalData = ''
    if request.method == "POST":
        poNo = request.form.get('poNum')
        cur = mysql.connection.cursor()
        query = """SELECT * FROM mydb.lines207 WHERE POs207_poNo207 = %s"""
        cur.execute(query, [poNo])
        data = cur.fetchall()
        globalData = data
        cur.close()

    return render_template('line.html', data=globalData)

if __name__ == "__main__":
    app.run(debug=True)