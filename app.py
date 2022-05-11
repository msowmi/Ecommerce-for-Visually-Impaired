from flask import Flask,redirect, request, url_for, render_template
import sqlite3 as sql

app=Flask(__name__)

class DB:
    def _init_(self, name = 0):
         self._name = name
         self._lid = 0
         self._tot=0

    # getter method
    def get_name(self):
        return self._name

    # setter method
    def set_name(self, x):
        self._name = x
    def get_lid(self):
        return self._lid

    # setter method
    def set_lid(self, x):
        self._lid = x

    def get_tot(self):
        return self._tot

    # setter method
    def set_tot(self, x):
        self._tot = x
obj=DB()
@app.route('/')
def home():
    try:
        lid=obj.get_lid()
        print(lid)
        return render_template('index.html',data=lid)
    except Exception as e:
        return render_template('index.html')


@app.route('/login')
def login():
    # obj._lid=0
    return render_template('login copy.html')
@app.route("/login", methods = ["GET","POST"])
def Login():

    l_id = request.form["logname"]
    l_pass  = request.form["logpass"]

    tab=l_id+l_pass
    #print("name")
    if request.method == 'POST':
        print("name")
        l_id = request.form["logname"]
        l_pass  = request.form["logpass"]

        tab=l_id+l_pass
        print(tab)
        obj.set_name(tab)
        obj.set_lid(l_id)
        return redirect(f"/cart")

    return render_template('invalid.html',invalid='Please enter a valid data')

@app.route('/sign')
def sign():
    return render_template('signup copy.html')

@app.route("/regis",methods=["GET","POST"])
def regis():
    u_id = request.values.get("signu_id")
    s_pass  = request.values.get("sign_pass")
    print(u_id)
    print(s_pass)
    table_name=u_id+s_pass
    print(table_name)
    try:
        conn=sql.connect('main.db')

        print("Opened database successfully")
        create="CREATE TABLE "+table_name+" (detail TEXT, cred TEXT)"
        conn.execute(create)
        #conn.execute("select * from credential")

        print("Table created successfully")
        conn.close()
        return render_template("success.html")
    except:
        # print("dsa")
        return render_template("invalid.html", a="Username and password are already taken. Try another.")



@app.route("/cart",methods = ["GET","POST"])
def cart():
    tab=obj.get_name()
    lid=obj.get_lid()
    print(lid)
    if request.method == 'GET':
        print(f"Your name is {tab}")
        try:
            con = sql.connect("main.db")
            con.row_factory = sql.Row
            cur = con.cursor()
            a=f"select * from {tab}"
            print(a)
            cur.execute(a)
            return render_template('index.html',data=lid)
        except :
            return render_template('invalid.html',invalid='Please enter a valid data')

    if request.method == 'POST':
        detail = request.values.get("detail")
        credential  = request.values.get("credential")
        print(detail)
        with sql.connect("main.db") as con:
                cur = con.cursor()
                ins="INSERT INTO "+tab+f" (detail,cred) VALUES {(detail,credential)}"
                print(ins)
                cur.execute(str(ins))

                con.commit()
                con.row_factory = sql.Row
                print("das")
                cur = con.cursor()
                a=f"select * from {tab}"
                print(a)
                cur.execute(a)
                print("dfaa")
                rows = cur.fetchall()
                print(rows)
                name=[]
                price=[]
                dict={}
                for r in rows:
                    price.append(int(r['cred']))
                print(sum(price))
                obj.set_tot(sum(price))

                return render_template("cart.html",rows = rows,tab=tab,sum=sum(price),data=lid)
        # return render_template("cart.html",a="values added successfully",tab=tab)






@app.route("/list",methods = ["GET","POST"])
def list_details():
    lid=obj.get_lid()
    tab=obj.get_name()
    #tab = request.form["tabname"]
    print(tab)
    con = sql.connect("main.db")
    con.row_factory = sql.Row
    print("das")
    cur = con.cursor()
    a=f"select * from {tab}"
    print(a)
    cur.execute(a)
    print("dfaa")
    rows = cur.fetchall()
    print(rows)
    for r in rows:
        print(r)

    return render_template("cart.html",rows = rows,tab=tab,data=lid)


@app.route('/kidswear', methods = ['GET', 'POST'])
def kidswear():
    lid=obj.get_lid()
    return render_template('kidswear.html',data=lid)
@app.route('/about', methods = ['GET', 'POST'])
def about():
    lid=obj.get_lid()
    return render_template('about.html',data=lid)
@app.route('/contact', methods = ['GET', 'POST'])
def contact():
    lid=obj.get_lid()
    return render_template('contact.html',data=lid)
@app.route('/earring', methods = ['GET', 'POST'])
def earring():
    lid=obj.get_lid()
    return render_template('earring.html',data=lid)
@app.route('/frock', methods = ['GET', 'POST'])
def frock():
    lid=obj.get_lid()
    return render_template('frock.html',data=lid)
@app.route('/girl', methods = ['GET', 'POST'])
def girl():
    lid=obj.get_lid()
    return render_template('girl.html',data=lid)
@app.route('/handbag', methods = ['GET', 'POST'])
def handbag():
    lid=obj.get_lid()
    return render_template('handbag.html',data=lid)
@app.route('/jacket', methods = ['GET', 'POST'])
def jacket():
    lid=obj.get_lid()
    return render_template('jacket.html',data=lid)
@app.route('/jeans', methods = ['GET', 'POST'])
def jeans():
    lid=obj.get_lid()
    return render_template('jeans.html',data=lid)
@app.route('/kurta', methods = ['GET', 'POST'])
def kurta():
    lid=obj.get_lid()
    return render_template('kurta.html',data=lid)

@app.route('/mi', methods = ['GET', 'POST'])
def mi():
    lid=obj.get_lid()
    return render_template('mi.html',data=lid)
@app.route('/productDetails', methods = ['GET', 'POST'])
def productDetails():
    lid=obj.get_lid()
    return render_template('productDetails.html',data=lid)
@app.route('/products', methods = ['GET', 'POST'])
def products():
    lid=obj.get_lid()
    return render_template('products.html',data=lid)

@app.route('/sandal', methods = ['GET', 'POST'])
def productDetailsi():
    lid=obj.get_lid()
    return render_template('sandal.html',data=lid)

@app.route('/slippers', methods = ['GET', 'POST'])
def slippers():
    lid=obj.get_lid()
    return render_template('slippers.html',data=lid)
@app.route('/sneakers', methods = ['GET', 'POST'])
def sneakers():
    lid=obj.get_lid()
    return render_template('sneakers.html',data=lid)
@app.route('/success', methods = ['GET', 'POST'])
def success():
    lid=obj.get_lid()
    return render_template('success.html',data=lid)
@app.route('/success2', methods = ['GET', 'POST'])
def success2():
    lid=obj.get_lid()
    return render_template('success2.html',data=lid)

@app.route('/purchase', methods = ['GET', 'POST'])
def purchase():
    total=obj.get_tot()
    uname=obj.get_lid()

    return render_template('purchase.html',total=total,data=uname)

if __name__=="__main__":
    app.run(debug=True)
