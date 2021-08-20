
import pyshorteners
url_name=input("Enter url :")
s=pyshorteners.Shortener().tinyurl.short(url_name)
print("Your shorted url :",s)