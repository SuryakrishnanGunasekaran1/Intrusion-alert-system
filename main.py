from flask import Flask
from flask import Flask, render_template, Response, redirect, request, session, abort, url_for
from camera import VideoCamera
from datetime import datetime
from datetime import date
import datetime
import random
from random import seed
from random import randint
from flask_mail import Mail, Message
from flask import send_file
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
import threading
import os
import base64
import time
import shutil
import imagehash
import hashlib
import PIL.Image
from PIL import Image
from PIL import ImageTk
import urllib.request
import urllib.parse
from urllib.request import urlopen
import webbrowser
#mac
import uuid
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  charset="utf8",
  database="login_security"
)


app = Flask(__name__)
##session key
app.secret_key = 'abcdef'
#####
##email
mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": "pospointofsalespos@gmail.com",
    "MAIL_PASSWORD": "ozopdivmnigvvaub"
}

app.config.update(mail_settings)
mail = Mail(app)
#######

@app.route('/',methods=['POST','GET'])
def index():
    cnt=0
    act=""
    msg=""
    ff=open("det.txt","w")
    ff.write("1")
    ff.close()

    ff1=open("photo.txt","w")
    ff1.write("1")
    ff1.close()

    ff11=open("img.txt","w")
    ff11.write("1")
    ff11.close()

    
 
    #import uuid
    #mac_address = uuid.getnode()
    #mac = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])
    #print(mac)

    ########
    
    ########

    if request.method=='POST':
        uname=request.form['uname']
        pass1=request.form['pass']
        
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM register where uname=%s && pass=%s",(uname, pass1))
        cnt = mycursor.fetchone()[0]
        if cnt>0:
            msg="success"
            session['username'] = uname
            mycursor.execute("update register set log_st=0 where uname=%s",(uname,))
            mydb.commit()
            return redirect(url_for('userhome'))
       
            
        else:
            mycursor.execute("SELECT count(*) FROM register where uname=%s",(uname,))
            cc = mycursor.fetchone()[0]
            if cc>0:
            
                msg="Username/Password is wrong!"
                mycursor.execute("SELECT * FROM register where uname=%s",(uname,))
                dd = mycursor.fetchone()
                log=dd[10]
                vid=dd[0]
                if log<3:
                    mycursor.execute("update register set log_st=log_st+1 where uname=%s",(uname,))
                    mydb.commit()
                else:
                    return redirect(url_for('add_photo',vid=vid))
            else:
                msg="Username/Password has wrong!"

    return render_template('index.html',msg=msg,act=act)


#########################

@app.route('/register',methods=['POST','GET'])
def register():
    msg=""
    act=""
    if request.method=='POST':
        name=request.form['name']
        
        mobile=request.form['mobile']
        email=request.form['email']
        city=request.form['city']
        desig=request.form['desig']
        uname=request.form['uname']
        pass1=request.form['pass']
        
        
        now = datetime.datetime.now()
        rdate=now.strftime("%d-%m-%Y")
        mycursor = mydb.cursor()

        mycursor.execute("SELECT count(*) FROM register where uname=%s",(uname, ))
        cnt = mycursor.fetchone()[0]
        if cnt==0:
            ff2=open("un1.txt","w")
            ff2.write(uname)
            ff2.close()
            
            mycursor.execute("SELECT max(id)+1 FROM register")
            maxid = mycursor.fetchone()[0]
            if maxid is None:
                maxid=1
            sql = "INSERT INTO register(id, name, mobile, email, city,  desig, uname, pass, rdate, fimg) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            val = (maxid, name, mobile, email, city, desig, uname, pass1, rdate, '')
            
            mycursor.execute(sql, val)
            mydb.commit()            
            #print(mycursor.rowcount, "record inserted.")
            msg="success"
            
        else:
            msg="Username Already Exist!"
    return render_template('register.html',msg=msg)



@app.route('/login_admin', methods=['POST','GET'])
def login_admin():
    result=""
    ff1=open("photo.txt","w")
    ff1.write("1")
    ff1.close()
    if request.method == 'POST':
        username1 = request.form['uname']
        password1 = request.form['pass']
        mycursor = mydb.cursor()
        mycursor.execute("SELECT count(*) FROM admin where username=%s && password=%s",(username1,password1))
        myresult = mycursor.fetchone()[0]
        if myresult>0:
            result=" Your Logged in sucessfully**"
            return redirect(url_for('admin')) 
        else:
            result="Your logged in fail!!!"
                
    
    return render_template('login_admin.html',result=result)



@app.route('/add_photo',methods=['POST','GET'])
def add_photo():
    st=""
    name=""
    mobile=""
    mess=""
    vid = request.args.get('vid')
    act = request.args.get('act')
    ff1=open("photo.txt","w")
    ff1.write("2")
    ff1.close()

    ff2=open("bc.txt","r")
    bc=ff2.read()
    ff2.close()
    
    if request.method=='GET':
        
        ff=open("user.txt","w")
        ff.write(vid)
        ff.close()
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM register where id=%s",(vid, ))
    data = cursor.fetchone()
    user="u"+str(vid)
        
    if request.method=='POST':
        vid=request.form['vid']
        fimg="v"+vid+".png"

        
    
        cursor.execute('update register set fimg=%s WHERE id = %s', (fimg, vid))
        mydb.commit()
        shutil.copy('faces/f1.png', 'static/f1.jpg')

        return redirect(url_for('check',vid=vid))
        
        
    return render_template('add_photo.html',data=data, vid=vid,bc=bc)

@app.route('/check',methods=['POST','GET'])
def check():
    st=""
    name=""
    mobile=""
    mess=""
    vid = request.args.get('vid')

    ff2=open("bc.txt","r")
    bc=ff2.read()
    ff2.close()

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM register where id=%s",(vid, ))
    ds = cursor.fetchone()
    uname=ds[6]
    name=ds[1]
    mobile=ds[2]
    email=ds[3]
    

    mac_address = uuid.getnode()
    mac = ':'.join(['{:02x}'.format((mac_address >> elements) & 0xff) for elements in range(0,8*6,8)][::-1])
    print(mac)

    cursor.execute("SELECT max(id)+1 FROM report")
    maxid = cursor.fetchone()[0]
    if maxid is None:
        maxid=1

    fn="F"+str(maxid)+".jpg"
    sql = "INSERT INTO report(id, uname, filename, mac_address) VALUES (%s, %s, %s, %s)"
    val = (maxid, uname, fn, mac)
    
    cursor.execute(sql, val)
    mydb.commit()

    shutil.copy('static/f1.jpg', 'static/upload/'+fn)

    cursor.execute('update register set log_st=0 WHERE id = %s', (vid,))
    mydb.commit()
    ##send mail
    mess="Dear "+name+", Someone access your login, Mac Address: "+mac
    with app.app_context():
        msg = Message(subject="Login Access", sender=app.config.get("MAIL_USERNAME"),recipients=[email], body=mess)
        with app.open_resource("static/upload/"+fn) as fp:  
            msg.attach("static/upload/"+fn, "images/jpeg", fp.read())
        mail.send(msg)
    

    return render_template('check.html',vid=vid,mobile=mobile,mess=mess,name=name,bc=bc)

@app.route('/userhome',methods=['POST','GET'])
def userhome():
    msg=""
    act=""
    uname=""
    if 'username' in session:
        uname = session['username']
        
    f1=open("user.txt",'r')
    vid=f1.read()
    f1.close()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM register where uname=%s",(uname, ))
    data = mycursor.fetchone()
    
    
    return render_template('userhome.html',msg=msg,act=act,data=data)

@app.route('/view_report',methods=['POST','GET'])
def view_report():
    st=""
    uname=""
    if 'username' in session:
        uname = session['username']
    

    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM report where uname=%s order by id desc",(uname, ))
    data = cursor.fetchall()

    return render_template('view_report.html',data=data)


@app.route('/cap',methods=['POST','GET'])
def cap():
    msg=""
    vid = request.args.get('vid')
    ff2=open("bc.txt","r")
    bc=ff2.read()
    ff2.close()

    
    mess="Someone Access your Login"

    cursor = mydb.cursor()
    cursor.execute('update register set log_st=0 WHERE id = %s', (vid,))
    mydb.commit()
    
    cursor.execute("SELECT * FROM register where id=%s",(vid, ))
    ds = cursor.fetchone()
    uname=ds[6]
    cursor.execute("SELECT * FROM report where uname=%s order by id desc",(uname, ))
    ds1 = cursor.fetchone()
    mac=ds1[3]
    dt=ds1[4]
    
        
    return render_template('cap.html',msg=msg,bc=bc,vid=vid,mac=mac,dt=dt)

    

    

@app.route('/upload',methods=['POST','GET'])
def upload():
    msg=""
    
    act = request.args.get('act')
    f1=open("user.txt",'r')
    vid=f1.read()
    f1.close()

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM register where id=%s",(vid, ))
    data = mycursor.fetchone()

    if request.method=='POST':
        file = request.files['file']

        fname=file.filename
        file.save(os.path.join("static/upload", fname))
        ##store
        
        mycursor.execute("SELECT max(id)+1 FROM user_files")
        maxid = mycursor.fetchone()[0]
        if maxid is None:
            maxid=1
        sql = "INSERT INTO user_files(id,vid,upload_file) VALUES (%s, %s, %s)"
        val = (maxid,vid,fname)
        mycursor.execute(sql,val)
        mydb.commit()
        
        msg="Uploaded success.."
        return redirect(url_for('upload'))
    
    mycursor.execute("SELECT * FROM user_files where vid=%s",(vid, ))
    data2 = mycursor.fetchall()

    if act=="del":
        did=request.args.get('did')
        mycursor.execute("delete from user_files where id=%s",(did, ))
        mydb.commit()
        return redirect(url_for('upload'))
    return render_template('upload.html',msg=msg,act=act,vid=vid,data=data,data2=data2)

@app.route('/down', methods=['GET', 'POST'])
def down():
    fn = request.args.get('fname')
    path="static/upload/"+fn
    return send_file(path, as_attachment=True)



@app.route('/logout')
def logout():
    # remove the username from the session if it is there
    #session.pop('username', None)
    return redirect(url_for('index'))

def gen(camera):
    
    while True:
        frame = camera.get_frame()
        
        
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
@app.route('/video_feed')
        

def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True,host='0.0.0.0', port=5000)
