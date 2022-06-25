from flask import Flask,request,session,redirect,url_for,send_from_directory,render_template,flash,send_file
from werkzeug.utils import secure_filename
import mysql.connector
import random
import os
from datetime import datetime
UPLOAD_FOLDER="D:/Assignment Tracker/uploaded_files"

app = Flask(__name__)
app.secret_key = "some_random_key"
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER



@app.route('/student_profile')
def student_profile():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                if 'name' in session:
                    name = session['name']
                    query=f"""select * from user where name='{session['name']}';"""
                    cursor.execute(query)
                    result = cursor.fetchall()
    except Exception as e:
        print(e)

    print(session)
    page = render_template("student_profile.html", records=result, name=name)
    return page
@app.route('/view_assignment') 
def view_assignment():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                query=f"""select * from assignment;"""
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
    except Exception as e:
        print(e)

    
    page = render_template('view_assignment.html', records=result)
    return page


@app.route('/upload')
def upload():
   return render_template('upload.html')
 


 
# @app.route('/uploader', methods = ['GET', 'POST'])
# def upload_file():
    # if request.method == 'POST':
       # f = request.files['file']
       # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
       # return 'file uploaded successfully'
       
       
       

   
       
@app.route('/uploader',methods=["GET","POST"])        
def upload_file():
    submissionid=str(random.randint(0,10000))
    
    msg=''
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                if request.method == 'POST':
                    submission_date = datetime.now()
                    f = request.files['file']
                    f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
                    
                    u1 = f"""select userid from user where name='{session['name']}' ;"""
                    cursor.execute(u1)
                    userid_record=cursor.fetchall()
                    userid=userid_record[0]
                    
                    title=request.form['title']
                    
                    a1 = f"""select assignmentid from assignment where title='{title}';"""
                    cursor.execute(a1)
                    assignmentid_rec=cursor.fetchone()
                    print(userid_record)
                    print(assignmentid_rec)
                    
                    query=f"""insert into submission(submissionid,assignmentid,userid,submission_date,solution)values('{submissionid}','{assignmentid_rec[0]}','{userid[0]}','{submission_date}','{f.filename}');"""
                    print(query)
                    cursor.execute(query)
                    connection.commit()
                    msg = 'You have successfully uploaded new assignment !'
                    return msg
            
    except Exception as e:
        print(e)    

    return render_template('student_profile.html') 
 
@app.route('/check_status') 
def check_status():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                if 'name' in session:
                    name=session['name']
                    u1 = f"""select userid from user where name='{session['name']}' ;"""
                    cursor.execute(u1)
                    userid_record=cursor.fetchall()
                    userid=userid_record[0]
                    print(userid)
                    print(u1)
                    query2 = f"""select submissionid, assignmentid,userid,status from submission where userid ='{userid[0]}';"""
                    cursor.execute(query2)
                    result = cursor.fetchall()
                    print(result)
    except Exception as e:
        print(e)

    
    page = render_template('check_status.html', records=result)
    return page


@app.route('/teacher_profile')
def teacher_profile():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                if 'name' in session:
                    name = session['name']
                    query=f"""select * from user where name='{session['name']}';"""
                    cursor.execute(query)
                    result = cursor.fetchall()
    except Exception as e:
        print(e)

    print(session)
    page = render_template("teacher_profile.html", records=result, name=name)
    return page

@app.route('/publish_assignment',methods=["GET","POST"])
def publish_assignment():
    assignmentid=str(random.randint(0,10000))
    msg=''
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                if request.method == 'POST':
                
                    title = request.form['title']
                    description = request.form['description']
                    due_date = request.form['due_date']
                    
                    query=f"""insert into assignment(assignmentid,title, description, due_date)values('{assignmentid}','{title}','{description}','{due_date}');"""
                    print(query)
                    cursor.execute(query)
                    connection.commit()
                    msg = 'You have successfully added new assignment !'
                    return redirect(url_for('teacher_profile'))
            
    except Exception as e:
        print(e)    

    return render_template('publish_assignment.html', msg = msg) 

    
    

           
@app.route('/view_solution') 
def view_solution():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                query=f"""select * from submission;"""
                print(query)
                cursor.execute(query)
                result = cursor.fetchall()
    except Exception as e:
        print(e)

    
    page = render_template('view_solution.html', records=result)
    return page  
    
@app.route('/download/<string:filename>', methods=['GET'])
def download(filename):
   print(filename)
   uploads=UPLOAD_FOLDER
   return send_file(uploads+'/'+filename, as_attachment=True)
   # with open(uploads+'/'+filename,'r') as fp:
       # return fp.read()
   # return send_from_directory(directory=uploads, filename=filename)
    
@app.route('/status',methods=['POST'])
def status():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                if request.method == 'POST':
                    status = request.form['status']
                    submissionid = request.form['submissionid']
                    query = f"""update submission set status = '{status}' where submissionid ='{submissionid}';"""
                    cursor.execute(query)
                    connection.commit()
    except Exception as e:
        print(e)    
    return render_template('view_solution.html')
@app.route('/gettrack_ofassignments')
def gettrack_ofassignments():   
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                    query=f"""select * from submission;"""
                    cursor.execute(query)
                    result = cursor.fetchall()
    except Exception as e:
        print(e)
    page = render_template("gettrack_ofassignments.html", records=result)
    return page

@app.route('/get_approved_cnt') 
def get_approved_cnt():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                    query=f"""select name,email_address,mobile_number from user where userid in (select userid from submission where status="approved") ;"""
                    cursor.execute(query)
                    result = cursor.fetchall()
    except Exception as e:
        print(e)
    page = render_template("get_approved_cnt.html", records=result)
    return page





@app.route('/get_rejected_cnt')
def get_rejected_cnt():
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                    query=f"""select name,email_address,mobile_number from user where userid in (select userid from submission where status="rejected") ;"""
                    cursor.execute(query)
                    result = cursor.fetchall()
    except Exception as e:
        print(e)
    page = render_template("get_rejected_cnt.html", records=result)
    return page

    

                    
        
        
@app.route('/login', methods=["GET", "POST"])
def login():
    msg=''
    if request.method == "GET":
        page = render_template("login.html")
        return page
    elif request.method == "POST":
        userid = request.form['name']
        password = request.form['password']
        
        all_users = getuser_from_userid(userid)
        
        user_type = get_typeofuser(userid)
        
        if len(all_users) == 0:
            return render_template("login.html")
            
        elif len(all_users) > 1:
            raise Exception(f"Multiple users with same userid present")

        user = all_users[0]
        type = user_type[0]
        print(user[1])
        
        if user[2] == password and type[0] == "student":
            
            session['name'] = request.form['name']
            
            return redirect(url_for("student_profile"))
        elif user[2] == password and type[0] == "teacher":
            
            session['name'] = request.form['name']
            
            return redirect(url_for("teacher_profile"))
        elif user[2] != password:
            msg="Password is incorrect"
            return render_template("login.html",msg1=msg)
            
def getuser_from_userid(userid):
    query = f"""select * from user where name = '{userid}';"""
    print(query)
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
    except Exception as e:
        print(e)
        return None
    return result

    
def get_typeofuser(userid):
    query = f"""select type_of_user from user where name='{userid}' ;"""
    print(query)
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
    except Exception as e:
        print(e)
        

    return result
@app.route('/forgot_password',methods=['GET','POST'])
def forgot_password():
    msg=''
    
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                if request.method == 'POST' and 'password' in request.form:
                    password = request.form['password']
                    query = f""" update user set password = '{password}' where name = '{session['name']}' """
                    cursor.execute(query)
                    connection.commit()
                    msg='Password is changed successfully..!!'
    except Exception as e:
        print(e)
    page = render_template('forgot_password.html',msg1=msg)
    return page

@app.route('/register', methods =['GET', 'POST'])
def register():
    userid=str(random.randint(0,10000))
    msg=''
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                if request.method == 'POST' and 'name' in request.form and 'password' in request.form and 'mobile_number' in request.form and 'email_address' in request.form and 'type_of_user' in request.form:
                    name = request.form['name']
                    password = request.form['password']
                    mobile_number= request.form['mobile_number']
                    email_address = request.form['email_address']
                    type_of_user = request.form['type_of_user']
                    query=f"""insert into user(userid,name, password, mobile_number, email_address,type_of_user)values('{userid}','{name}','{password}','{mobile_number}','{email_address}','{type_of_user}');"""
                    
                    cursor.execute(query)
                    connection.commit()
                    msg = 'You have successfully registered !'
                    
                    return redirect(url_for('login'))
            
    except Exception as e:
        print(e)    

    return render_template('register.html', msg = msg)
@app.route('/delete')
def delete():
    msg="Your account is deleted successfully"
    if 'name' in session:
        name = session['name']
    print(name)
    query=f"""delete from user where name='{name}';"""
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                
                cursor.execute(query)
                connection.commit()
                
    except Exception as e:
        print(e)    
    
    page = render_template("home_page.html",msg=msg)
    return page
    
    
@app.route('/update',methods=["GET","POST"])
def update():
    msg=''
    
    try:
        with mysql.connector.connect(host="localhost",user="root",password="root@123",database="assignment_tracking") as connection:
            with connection.cursor() as cursor:
                cursor = connection.cursor()
                if request.method == 'POST' and 'email_address' in request.form:
                    email_address = request.form['email_address']
                    query = f"""update user set email_address = '{email_address}'where name='{session['name']}';"""
                    cursor.execute(query)
                    connection.commit()
                    msg = 'You have successfully updated email_address!!'
    except Exception as e:
        print(e)    
    
    return render_template('update.html', msg = msg)
    
       
@app.route('/home_page')
def home_page():
    return render_template("home_page.html")  
    
@app.route('/logout')
def logout():
    session.pop('name')
    return redirect(url_for("home_page"))

    
    
    
@app.route('/')
def root_page():
    return redirect(url_for("home_page"))

 

        
if __name__=="__main__":

    app.secret_key = "some_random_key"
    app.run(host="0.0.0.0", port=50000) 

















