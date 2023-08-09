# https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
import pyqrcode


url = "https://m.booking.naver.com/booking/13/bizes/369432"
# url = "https://m.booking.naver.com/booking/13/bizes/369432?theme=place&entry=pll&area=pll"
qrcode = pyqrcode.create(url)
qrcode.svg("booking.svg", scale =8)