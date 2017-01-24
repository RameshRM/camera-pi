from flask import Flask
import picamera

print "foo"

app = Flask(__name__)
@app.route("/start")

def start():
  #camera=picamera.PiCamera()
 # camera.start_recording()
  return "Start"

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')


