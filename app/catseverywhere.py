from flask import Flask, render_template, request, redirect
import ast
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Taneil"
    name = "myself"
    return render_template('index.html', author=author, name=name)

emailfile=open("email.txt","r")
mystr= emailfile.readline()
email_addresses=ast.literal_eval(mystr)
emailfile.close()



@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    print(email_addresses)
    mysave= open("email.txt","w")
    mystr= str(email_addresses)
    mysave.write(mystr)
    mysave.close()
    return redirect('/')

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run()


