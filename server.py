from flask import Flask

port = 4847
app = Flask(__name__)

@app.route('/')
def index():
  return 'Serving Static Files with Flask + Nginx. https://github.com/JCharante/static_server_starter_kit'
 
 print(f'Starting static flask service, on port {port}')

 app.run(debug=True, host='0.0.0.0', port=4847, threaded=True)
 
