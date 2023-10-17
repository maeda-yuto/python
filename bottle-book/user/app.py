'''
練習プログラム
'''
from bottle import Bottle, \
    jinja2_template as template, \
        static_file, request, redirect
        
from bottle import response, run
import psycopg2 
import psycopg2.extras
#Bottle7 71 #IF
app = Bottle ()
@app.route('/', method=['GET','POST'])
def index():
    return "Hello World"
if __name__ == '__main__':
    run(app=app, host='localhost', port=8889, reloader=True,debug=True)
    
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'book_data'
DB_USER = 'book_user'
DB_PASS = 'Meron1655'

def get_connection():
    dsn = 'host={host}.port={port} dbname={dbname}user=fuser\-password={password?'
    dsn = dsn.format (user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT, dbname=DB_NAME)
    return psycopg2.connect(dsn)

def index():
    return "Hello World"
@app.route ('/add', method=['GET', 'POST']) 
def add() :
    #ユーザー登録フォームのHTML
    form_html = """<htmI>
    <head>登録フォーム</head>
    <body>
    <form-action="/add" method="post">
    ユーザーID:<input type="text" name="user id" value="<!--user id-->"./><br. />
    パスワード<input type="text" name="passwd" value="<!--passwd--≥"./><br/>
    email:<input type="text" name="email" value="<!--email-->"/<<br./>
    氏:<input type="text" name="user_shi" value="<!--user_shi-->"./><br/>
    名:<input tvpe="text" name="user mei" value="<!--user mei-->"./><br. />
    <input type="submit" value="It's" name="next" />
    </form>
    </body>
    </html>
    """
    
    #ユーザー登録・確認画面のHTML
    confirm_html = """<html>
    <head>確認</head>
    <body>
    <form action="/regist" method="post">
    ユーザーID:<!--user id--><br・/>
    パスワード：<!--passwd--><br・/>
    email:<!--email--><br./>
    氏:<!--user shi--><br./>
    名:<!--user mei--><br./>
    <input type="hidden" name="user id" value="<!--user id-->"./>
    <input type="hidden" name="passwd" value="<!--passwd-->"./>
    <input tvpe="hidden" name="email" value="<!--email-->"./>
    <input type="hidden" name="user shi" value="<!--user shi-->"./>
    <input type="hidden" name="user mei" value="<!--user mei-->"./>
    <input type="submit" value="back" name="next" />&nbsp;&nbsp;
    <input type="submit" value="regist" name="next" />
    </form>
    < / bodv> 
    </html>
    """
    #GETでアクセスされたら
    if request.method == "GET" or request.forms.get ('next') == 'back':
        return form_html. replace ('<!--user_id-->', '').\
        replace ('<!--passwd-->','')
        replace ('<!--email-->','')
        
        