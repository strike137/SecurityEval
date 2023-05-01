from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/xss")
def xss():
    '''
    get the username from the request,  make a response with it and return it
    '''
    username = request.args.get('username')
    response = make_response(username)
    return response
