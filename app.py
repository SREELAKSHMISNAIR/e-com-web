from flask import Flask, render_template, jsonify, request
from database import checkadminlogin

app = Flask(__name__)


@app.route("/")
def index_page():
  return render_template('admin-login.html')


@app.route("/checklogin", methods=['post'])
def adminlogin():
  #data = jsonify(request.form)
  adusername = request.form.get('adusername')
  adpassword = request.form.get('adpassword')
  checkadminlogin(adusername, adpassword)
  return "credentials verified"


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True, port=8081)
