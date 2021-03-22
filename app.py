import datetime

from flask import Flask

app = Flask(__name__)

@app.route('/date')
def date():
    now = datetime.datetime.now()
    textDate =  now.strftime('%c')
    return { 'date': textDate }

if __name__ == '__main__':    
    app.run()
