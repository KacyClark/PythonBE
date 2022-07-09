from flask import Flask

print("hello from server")
app = Flask("server")

@app.get('/')
def home():
    return "Hello from flask server"

@app.get("/test")
def test():
    return "This is just a test"

    # GET /about
    #show your name
@app.get("/about")
def about():
    return "Kacy Clark"





#######################################################
##########  API ENDPOINTS = PRODUCTS  #################
#######################################################



@app.get("/api/version")
def version():
    return "1.0"



app.run(debug=True)
