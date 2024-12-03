from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# 默认用户名和密码
default_username = "caiji_233"
default_password = "114514"

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == default_username and password == default_password:
            return redirect('/login.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()