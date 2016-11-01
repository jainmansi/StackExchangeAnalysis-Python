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

		searchUrl = "https://api.stackexchange.com/2.2/tags?key=QfgSYwzvIpLIqngtwggFPg((&page="+str(i)+"&pagesize=100&order=desc&sort=popular&site=stackoverflow";
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		#count = 0
		#for item in rec["items"]:
			#print (item)
    
		#print(count)

		name = "tags"

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
	
def fetchBadgesData():
	i = 1

	#key=QfgSYwzvIpLIqngtwggFPg((

	while i < 101:

		searchUrl = "https://api.stackexchange.com/2.2/badges?key=QfgSYwzvIpLIqngtwggFPg((&page="+str(i)+"&pagesize=100&order=desc&sort=rank&site=stackoverflow";
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		count = 0
		for item in rec["items"]:
			print (item)
    
		print(count)

		name = "badges"

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
		
		return;
		
def fetchQuestionsData():
	i = 1

	#key=QfgSYwzvIpLIqngtwggFPg((

	while i < 101:

		searchUrl = "https://api.stackexchange.com/2.2/questions?key=QfgSYwzvIpLIqngtwggFPg((&page="+str(i)+"&pagesize=100&fromdate=1293840000&todate=1477958400&order=desc&sort=votes&site=stackoverflow"
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		#count = 0
		#for item in rec["items"]:
			#print (item)
    
		#print(count)

		name = "questions"

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
		
def fetchUnansweredQuestionsData():
	i = 1

#key=QfgSYwzvIpLIqngtwggFPg((

	while i < 101:

		searchUrl = "https://api.stackexchange.com/2.2/questions/unanswered?key=QfgSYwzvIpLIqngtwggFPg((&page="+str(i)+"&pagesize=100&fromdate=1293840000&todate=1477958400&order=desc&sort=votes&site=stackoverflow"
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		#count = 0
		#for item in rec["items"]:
			#print (item)
		
		#print(count)

		name = "unansweredQuestions"

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
		
def fetchUsersData():
	i = 1

	#key=QfgSYwzvIpLIqngtwggFPg((

	while i < 101:

		searchUrl = "https://api.stackexchange.com/2.2/users?key=QfgSYwzvIpLIqngtwggFPg((&page="+str(i)+"&pagesize=100&order=desc&sort=reputation&site=stackoverflow"
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		#count = 0
		#for item in rec["items"]:
			#print (item)
		
		#print(count)

		name = "users"

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
fetchBadgesData()
fetchQuestionsData()
fetchUnansweredQuestionsData()
fetchUsersData()