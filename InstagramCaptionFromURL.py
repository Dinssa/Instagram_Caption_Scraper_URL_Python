# -*- coding: utf-8 -*-

"""
	Instragram Captions from a given url
	@author Emanuel Dinssa
	@contact https://www.linkedin.com/in/dinssa/
	
	This script illustrates how to extract the captions of public
	Instagram posts and can be extended to properly process emojis.
"""

import requests
from bs4 import BeautifulSoup

import re

'''Whatever URL you want (but has to be a public, not private, account)'''

url = ('https://www.instagram.com/p/BsnyFfxHBj7/')
    
response = requests.get(url)


'''Copies the html code of the entire page into our little soup bowl'''

soup = BeautifulSoup(response.text, 'html.parser')


'''Scan through the whole text and find anything within the <script> <\script> brackets'''

scripts = soup.find_all("script")


'''For each instance of <script> we check for the below keywords'''

for i in range(len(scripts)):
    if "edge_media_to_caption" in scripts[i].text:
        keyscript = scripts[i].text
   
    
'''Within the right script we then extract the caption from inbtween the START & END points
		START: "edge_media_to_caption":{"edges":[{"node":{"text":"
		END:  "}}]},"caption_is_edited"                                 			'''

try:
    found = re.search('{"node":{"text":"(.+?)"}}]},"caption_is_edited"',keyscript).group(1)
except AttributeError:
    found = ''    
    
    
'''1: No emoji processing'''
return(found)    

'''2: Partial lazy processing'''
#return(found.replace('\\u', ' \\ '))
