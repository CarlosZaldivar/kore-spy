# kore-spy

Simple project for Raspberry Pi that paired with https://github.com/blakeblackshear/rpi-hdmi-cec-rest should allow you to power on and off your TV just with Kore (Kodi's remote app).

kore-spy uses scapy to inspect incoming packets, so that when it detects a `System.Suspend` message, it can send a shutdown request to the CEC API. Powering a TV on is not as straight forward, because I didn't know how to listen to Wake-on-Lan messages on RPI. Instead of detecting WoL, the script detects a double home button click and treats it as a power on command.

Running two Docker containers just to turn a TV on and off is definitely not very efficient but at least it works (for me).