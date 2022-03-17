# @mharsch/node-red-serlcd

A Node-RED node for communicating with Sparkfun SerLCD boards


## Pre-requisite

Follow Sparkfun instructions for installing the [Qwiic_SerLCD_Py](https://github.com/sparkfun/Qwiic_SerLCD_Py)
Python package.  If you need to change the i2c address (which is persistent), use the python interface.
Try out the hello world from python first to make sure the display is working before moving on to this
Node-RED node (as we use the python under the hood).

## Install

Either use the Node-RED Menu - Manage Palette option to install, or run the following
command in your Node-RED user directory - typically `~/.node-red`

    npm install @mharsch/node-red-serlcd

## Usage

Send a string to the node to display on the LCD display.  This node follows the interface specified by
[node-red-node-pilcd](https://flows.nodered.org/node/node-red-node-pilcd)
e.g. send "clr:" to clear screen.  See example flow in this repo for extensions to the interface including
"contrast:" and "backlight:".


