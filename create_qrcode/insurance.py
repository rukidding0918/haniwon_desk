
import pyqrcode

url = 'https://insurance-claim.pay.naver.com'
qrcode = pyqrcode.create(url)

qrcode.svg('../assets/images/insurance.svg', scale=8)
# qrcode.png(
#     "insurance.png",
#     scale =8,
#     module_color=(44, 255, 0),
#     background=(22, 27, 41)
# )
