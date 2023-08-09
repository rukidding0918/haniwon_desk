# https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/
import pyqrcode


url = "https://m.place.naver.com/my/feed"
qrcode = pyqrcode.create(url)
qrcode.svg("./assets/images/review.svg", scale =8)