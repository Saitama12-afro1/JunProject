from base64 import decode
from main import app
with app.open_instance_resource("config.py") as f:
    config = f.read()
# s = str(config)
s =config.decode("utf-8")
print(s)