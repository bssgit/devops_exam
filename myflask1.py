from flask import Flask
 
 # create flask app
app = Flask(__name__)
   
 
   # add all the routes
   
@app.route("/", methods=["GET"])

#@app.route("/modules", methods=["GET"])
def root():
   return "welcome to ITIL exam................."

@app.route("/modules", methods=["GET"])

def modules():
  return "Modules: COSA, DEVOPS&ITIL, SECURITY CONCEPTS, FCN , PKI , NETWORK DEFENCE COUNTERMEASEURE"
@app.route("/me", methods=["GET"])

def me():
  return "PRN: 230344223008 , Name: BHARAT SURESH SHELAR , Phone number: 1234567890"
app.run(host="0.0.0.0", port=4000, debug=True)

