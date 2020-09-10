from flask import Flask,request
from flask_mysqldb import MySQL
import yaml
import json
app=Flask(__name__)
db=yaml.load(open('db.yaml'))
app.config['MYSQL_HOST']=db['mysql_host']
app.config['MYSQL_USER']=db['mysql_user']
app.config['MYSQL_PASSWORD']=db['mysql_password']
app.config['MYSQL_DB']=db['mysql_db']
mysql=MySQL(app)
@app.route('/session', methods=['GET'])
def get_data_session_id():
    data = request.data
    json_data = json.loads(data)
    sess = json_data["session"]
    cur = mysql.connection.cursor()
    cur.execute("SELECT sesskey From gms_active_logins")
    data = cur.fetchall()
    list_session_key =[]
    for row in data:
        for i in row:
            list_session_key.append(i)
    if sess in list_session_key:
        return "True"
    else:
        return "False"

if __name__=='__main__':
    app.run(debug=True)
