import hmac
import hashlib
import base64

dig = hmac.new(b'aloha', digestmod=hashlib.sha256).digest()
print(base64.b64encode(dig).decode())
