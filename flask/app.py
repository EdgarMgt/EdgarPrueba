#import 
    from flask import flask

#init app
app=flask(_name_)

#route
@app.route('/')
def index():
    return '<h1>MY Index</h1>'

#run the app
if __name__ == '__main__':
    app.run(debug=True)


