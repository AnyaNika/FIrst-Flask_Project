from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    now = datetime.now()
    date_time_now= now.strftime('%Y-%m-%d %H:%M')
    return f"<h2>Текущие дата и время:</h2><p>{date_time_now}</p>"

if __name__ == "__main__":
    app.run()