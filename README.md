# Acc(elerometer)2OSC
An accelerometer to open sound control (osc) python application that runs on a raspberry pi with a sense-hat attached. This was used as an input to a generated multimedia presentation so dancer's motions could contribute to the projected environment.

## Preperation
Only works with a raspbery pi and a [sense-hat](https://www.adafruit.com/product/2738?src=raspberrypi)

### Nix
this repository has devenv setup so if you have it installed and direnv then everything should set it self up for you.

## Otherwise
`pip install -r requirements.txt`
Feel free to use venv or any other environment manager.

## Usage
`python acc2Osc.py`

Optionally you can include the `--ip` or `--port` switches to specify the location of the osc server to send messages too.
