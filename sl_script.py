import ssl
import urllib.request

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

ip = input("What ip address do you want to lookup:")

url = f"https://ipapi.co/{ip}/json"
contents = urllib.request.urlopen(url, context=ctx).read()
print(contents)
