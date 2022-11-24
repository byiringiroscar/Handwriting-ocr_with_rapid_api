import requests
from urllib.parse import urlparse
from decouple import config

API_KEY = config('API_KEY')
url = "https://pen-to-print-handwriting-ocr.p.rapidapi.com/recognize/"

file = r'G:\Projects\Python&AI\handwirting_ocr\testimage.jpg'

img_a = urlparse(file)
img_a = img_a.path
img_a = img_a.split('\\')
img_a = img_a[-1]
print(img_a)

payload={}
files=[
  ('srcImg',(img_a,open(file,'rb'),'image/jpeg'))
]



headers = {
  'X-RapidAPI-Key': F'{API_KEY}'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)