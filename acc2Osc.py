import argparse
import time

from pythonosc import udp_client

from sense_hat import SenseHat

sense = SenseHat()
sense.set_imu_config(True, False, False)

mins = {'x': 0, 'y': 0, 'z': 0}
maxes = {'x': 0.1, 'y': 0.1, 'z': 0.1}

def normValues(vs):
  out = {}
  for k in vs:
     mins[k] = min(vs[k], mins[k])
     maxes[k] = max(vs[k], maxes[k])
     out[k] = (vs[k] - mins[k]) / (maxes[k] - mins[k])
  return out

if __name__ == "__main__":
  update_freq = 30 #hz
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip", default="127.0.0.1",
      help="The ip of the OSC server")
  parser.add_argument("--port", type=int, default=57120,
      help="The port the OSC server is listening on")
  args = parser.parse_args()

  client = udp_client.SimpleUDPClient(args.ip, args.port)

  while (True):
    acc = sense.accel_raw
    norm_acc = normValues(acc)
    acc_values = [norm_acc['x'], norm_acc['y'], norm_acc['z']]
    print('acc["x"]: ' + str(acc['x']))
    client.send_message("/acc", acc_values)
    time.sleep(1/update_freq)
