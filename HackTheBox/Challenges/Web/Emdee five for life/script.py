import re
import requests
import hashlib

def remove_html_tags(response):

    html = response.text

    text_without_html_tags = re.sub(regex_to_clean, '', html)

    return text_without_html_tags

url = ""

regex_to_clean = re.compile('<.*?>')

session = requests.Session()

response = session.get(url)

text_without_html_tags = remove_html_tags(response)

str_to_hash = text_without_html_tags.split('string')[1].rstrip()

md5_hash = hashlib.md5(str_to_hash.encode('utf-8')).hexdigest()

data = dict(hash=md5_hash)

response = session.post(url, data=data)

print(response.text)

"""
Comment the above line and uncomment the below lines if you want to print
only the flag to the screen
"""

# text_without_html_tags = remove_html_tags(response)

# flag = '{' + text_without_html_tags.split('{')[1].strip()

# print(flag)