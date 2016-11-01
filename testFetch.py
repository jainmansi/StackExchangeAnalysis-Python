from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
import argparse
import json
import os
from time import gmtime, strftime
import time
import os

def fetchTagData():
	i = 1

#key=QfgSYwzvIpLIqngtwggFPg((

	while i < 101:

		searchUrl = "https://api.stackexchange.com/2.2/answers?key=QfgSYwzvIpLIqngtwggFPg((&order=desc&sort=activity&site=stackoverflow";
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		#count = 0
		#for item in rec["items"]:
			#print (item)
    
		#print(count)

		name = "testAnswers"

		def new_folder(name):
			if not os.path.exists(name):
				os.makedirs(name)
        
		for directory in os.listdir(): 
			if name!=directory:
				new_folder(name) 
                
		fname = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
		fname = name + "\\" + fname + '.json';

    
		json.dumps(rec)
		with open(fname ,'w')as f:
			json.dump(rec, f)
    
		i = i+1
		time.sleep(3)
    
		#P = json.load(open(fname))
		#print(P)
	
		return;
		
fetchTagData()