import os
from flask import Flask, request
import time
import requests
import json

def create_app():
  app = Flask(__name__)
  return app

def get_exec_time(appname):
  dirname = os.path.dirname(__file__)
  exectime_filename = os.path.join(dirname, appname+'.json')
  with open(exectime_filename, 'r') as exectime_file:
    # content = oplock_file.Read
    exectimejson = json.load(exectime_file)
  
  exectime = {}
  for each in exectimejson:
    exectime[each["name"]] = each["time"]
  return exectime

time.sleep(15)
app = create_app()

whoami = os.environ.get("WHOAMI")
replicas = ["paris", "tokyo", "singapore", "capetown", "newyork"]

def execute(appname, opname, params):
  url = "http://locker-"+whoami+":400"+str(replicas.index(whoami)+1)+"/jsonrpc" 
  print("locking rpc request to " + url, flush=True)
  # ACQUIRE REQUIRED LOCKS
  payload = {
        "method": "acquire_locks",
        "params": [appname, opname, params],
        "jsonrpc": "2.0",
        "id": 0,
    }
  response = requests.post(url, json=payload).json()

  print(response, flush=True)
  print("locks acquired", flush=True)
  # sleep the execution time
  exectime = get_exec_time(appname)
  # print(exectime[opname])
  time.sleep(exectime[opname] * 0.001)

  # release locks
  payload = {
        "method": "release_locks",
        "params": [response["result"]],
        "jsonrpc": "2.0",
        "id": 0,
    }
  response = requests.post(url, json=payload).json()

  print("locks released", flush=True)


@app.route('/')
def hello_world():
  return f'Hello world from {whoami} \n'

@app.route('/do', methods=['GET'])
def do_get():
  app = request.args.get('app', '')
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(app, op, params, flush=True)

  execute(app, op, params)
  
  return "done"

@app.route('/do', methods=['PUT'])
def do_put():
  app = request.args.get('app', '')
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(app, op, params, flush=True)

  execute(app, op, params)
  
  return "done"

@app.route('/do', methods=['DELETE'])
def do_delete():
  app = request.args.get('app', '')
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(app, op, params, flush=True)

  execute(app, op, params)
  
  return "done"

@app.route('/do', methods=['POST'])
def do_post():
  app = request.args.get('app', '')
  op = request.args.get('op', '')
  paramstring = request.args.get('params', '')

  params = {}
  for each in paramstring.split(","):
    kv = each.split("-")
    params[kv[0]] = kv[1]

  print(app, op, params, flush=True)

  execute(app, op, params)
  
  return "done"
