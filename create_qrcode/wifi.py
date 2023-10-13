# https://www.geeksforgeeks.org/wi-fi-qr-code-generator-using-python/
import pyqrcode


authentication_type = "WPA"
ssid = "bluehill"
password = "10091009"
hidden = False

url = f"WIFI:T:{authentication_type};S:{ssid};P:{password};H:{hidden};;"

qrcode = pyqrcode.create(url)
qrcode.svg("../assets/images/wifi.svg", scale =8)