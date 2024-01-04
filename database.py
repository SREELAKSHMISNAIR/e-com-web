from sqlalchemy import create_engine, text
import os

db_conn_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(db_conn_string,
                       connect_args={"ssl": {
                           "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def checkadminlogin(username, password):
  with engine.connect() as conn:
    query = text(
        "select * from users where username = :adusername AND password = :adpassword"
    )
    result = conn.execute(query, {
        "adusername": username,
        "adpassword": password
    })
    rows = result.all()
    if len(rows) == 0:
      return None
    else:
      return "credentials are correct"
