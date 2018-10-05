from flask import Flask, request, redirect, render_template
import cgi
import os
import re


app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():

    return render_template('edit.html')
               
@app.route("/", methods=["POST"])
def validate():
    user_name = request.form['user-name']
    p_word  = request.form['password']
    vfy_pwd  = request.form['verify-password']
    e_mail = request.form['email']
    u_error =''
    p_error =''
    v_error=''  
    e_error =''

    if user_name == '':
          u_error= 'That\'s not a valid Username' 
           

    if len(user_name) >20 or len(user_name) < 3: 
        u_error= 'That\'s not a valid Username' 
           
      
    if len(p_word) >20 or len(p_word) < 3:
        p_error= 'That\'s not a valid password'
            

    if p_word != vfy_pwd or p_word == '':
        v_error= 'Password didn\'t  match'

    if len(e_mail) > 0:
       if (len(e_mail) > 20 or len(e_mail) <3):
           e_error = 'That\'s not a valid email'
        

       elif e_mail.count(' ') >0:
            e_error = 'That\'s not a valid email'
         

       elif e_mail.count('@') != 1  or e_mail.count('.') !=1:
             e_error = 'That\'s not a valid email'

    #regular expression
    #mail ="EmailMatches:",len(re.findall("\w._%+-]{1,20}@[\w.-]{2,20}.[A-Za-z]{2,3}",e_mail))
       
        
    if not u_error and not p_error and not v_error and not e_error:        
            msg = user_name
            return redirect('/valid-msg?msg={0}'.format(msg)) 
    else:
       return render_template('edit.html',
                user_name=user_name,   
                u_error=u_error,
                p_word=p_word,
                p_error=p_error,
                vfy_pwd =vfy_pwd,
                v_error=v_error,
                e_error =e_error,
                e_mail=e_mail)              

@app.route("/valid-msg")
def valid():
    msg =request.args.get('msg') 
    #return '<h1> Welcome,  {0}! </h1>'.format(msg)
    return render_template('validation.html', msg = msg)
app.run()