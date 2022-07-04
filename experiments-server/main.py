from flask import Flask, render_template, send_file, request, jsonify
import requests
from replit import db
from time import sleep
import os


app = Flask(__name__, static_folder="static")

ips = []

#Bootstrap(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/experiments')
def experiments():
  experiment = request.args.get('experiment')
  if experiment.isdigit():
    return render_template('experiment.html')
  else:
    return "error", 404

@app.route('/ip', methods = ['POST'])
def ip_log():
  if request.json['value'].replace('.', '').isdigit():
    ips.append(request.json['value'])
  return "200"

@app.after_request 
def after_request_callback( response ): 
    if ".data" in request.url:
      return send_file("static/" + request.url.replace("http://roobarb.codes", ""))
    return response 

def database():
  while True:
    if len(ips) > 0:
      try:
        response = requests.get(f"https://geolocation-db.com/json/{ips[0]}&position=true").json()

        data = {
          'ip': ips[0],
          'country': response['country_name'],
          'city': response['city']
        }

        try:
          db["visitors"].append(data)
              
        except:
          db["visitors"] = [data]
        
        ips.pop()[0]
        
        visitors = db["visitors"]
        visitors_single = []
        already_gone = []
        for visitor in visitors:
          if (visitor['ip'] not in already_gone):
            visitors_single.append([visitor, visitors.count(visitor)])
            already_gone.append(visitor['ip'])
        
        for visitor_single in visitors_single:
          print("\nIP: " + visitor_single[0]['ip'])
          print("Country: " + visitor_single[0]['country'])
          print("City: " + visitor_single[0]['city'])
          print("Times Visited: " + str(visitor_single[1]) + "\n")
      except:
        print("INVALID")
            
    sleep(5)



#db_thread = threading.Thread(target=database, args=())
#db_thread.start()

app.run(host='0.0.0.0', port=8080)
