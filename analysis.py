import glob
import json
import pyexcel
import operator
import requests
import time
import csv

def mostPopularBadges():

	bronze_badge = {}
	silver_badge = {}
	gold_badge = {}

	for filename in glob.glob(r"badges\*.json"):
		with open(filename, 'r') as f:
			P = json.load(f)
			
			for item in P["items"]:
				#print(item)
				#print(item["rank"])
				if item["rank"] == "bronze":
					#print(item["rank"])
					bronze_badge[item["name"]] = item["award_count"]
					#print(item["name"])
					#print(item["award_count"])
				elif item["rank"] == "silver":
					silver_badge[item["name"]] = item["award_count"]
				elif item["rank"] == "gold":
					gold_badge[item["name"]] = item["award_count"]
						
						
	#print(bronze_badge)
	#print(silver_badge)
	#print(gold_badge)

	#bronze_badge_sorted = sorted(bronze_badge, key=bronze_badge.get, reverse=True)
	#silver_badge_sorted = sorted(silver_badge, key=silver_badge.get, reverse=True)
	#gold_badge_sorted = sorted(gold_badge, key=gold_badge.get, reverse=True)

	bronze_badge_sorted = sorted(bronze_badge.items(), key=operator.itemgetter(1), reverse = True)
	silver_badge_sorted = sorted(silver_badge.items(), key=operator.itemgetter(1), reverse = True)
	gold_badge_sorted = sorted(gold_badge.items(), key=operator.itemgetter(1), reverse = True)

	pyexcel.save_as(array = bronze_badge_sorted, dest_file_name = r'badges\BronzeBadgesSortedTest.csv')
	pyexcel.save_as(array = silver_badge_sorted, dest_file_name = r'badges\SilverBadgesSortedTest.csv')
	pyexcel.save_as(array = gold_badge_sorted, dest_file_name = r'badges\GoldBadgesSortedTest.csv')

	print(bronze_badge)

	#print(bronze_badge_sorted)
	
	return;
	
def FAQsOnMostPopularTags():
	tag_count = {}

	#Finding the most popular tag

	for filename in glob.glob(r"tags\*.json"):
		with open(filename, 'r') as f:
			P = json.load(f)
			
			try:
				for item in P["items"]:
					tag_count[item["name"]] = item["count"]
			except KeyError:
				print("Skipping a file...")
	tag_name_sorted = sorted(tag_count, key=tag_count.get, reverse=True)

	tag_value_sorted = sorted(tag_count.items(), key=operator.itemgetter(1), reverse = True)

	print("Top two tags of all times are {val}".format(val = tag_name_sorted[:2]))

	pyexcel.save_as(array = tag_value_sorted, dest_file_name = r'tags\TagsSorted.csv')

	#Getting top 3 questions for each of the three tags

	i = 0;

	while i < 2:

		searchUrl = "https://api.stackexchange.com/2.2/tags/"+tag_name_sorted[i]+"/faq?key=QfgSYwzvIpLIqngtwggFPg((&site=stackoverflow"
		r = requests.get(searchUrl, stream = True)

		#print(r.content)
		rec = dict(r.json())
		
		#print(rec)
		
		question_value = {}
		
		json.dumps(rec)
		#print(rec)
		filename = 'tags\\'+tag_name_sorted[i]+'.json'
		with open(filename ,'w')as f:
			json.dump(rec, f)
			
		with open(filename, 'r') as f:
			P = json.load(f)

		try:
			for item in P["items"]:
				impact_factor = item["view_count"] + item["score"]/2
				question_value[item["title"]] = impact_factor
		except KeyError:
			print("")
		
		question_sorted = sorted(question_value.items(), key=operator.itemgetter(1), reverse = True)
		

		pyexcel.save_as(array = question_sorted, dest_file_name = 'tags\\'+tag_name_sorted[i]+'.csv')
			
		i += 1
		
		return;
		
def comparingTrends():

	#Seggregating data according to time

	python_trend = {"2008":0,"2009":0,"2010":0,"2011":0,"2012":0,"2013":0,"2014":0,"2015":0,"2016":0}
	java_trend = {"2008":0,"2009":0,"2010":0,"2011":0,"2012":0,"2013":0,"2014":0,"2015":0,"2016":0}

	for filename in glob.glob(r"questions\*.json"):
		with open(filename, 'r') as f:
			P = json.load(f)
			
			try:
				for item in P["items"]:
					
					#year 2008
					
					if (item["creation_date"] > 1199145600 and item["creation_date"] < 1230767999):
						if "python" in item["tags"]:
							python_trend["2008"] += 1
						elif "java" in item["tags"]:
							java_trend["2008"] += 1
							
					#year 2009
					
					elif (item["creation_date"] > 1230768000 and item["creation_date"] < 1262303999):
						if "python" in item["tags"]:
							python_trend["2009"] += 1
						elif "java" in item["tags"]:
							java_trend["2009"] += 1
							
					#year 2010
					
					elif (item["creation_date"] > 1262304000 and item["creation_date"] < 1293839999):
						if "python" in item["tags"]:
							python_trend["2010"] += 1
						elif "java" in item["tags"]:
							java_trend["2010"] += 1
							
					#year 2011
					
					elif (item["creation_date"] > 1293840000 and item["creation_date"] < 1325375999):
						#print("here")
						if "python" in item["tags"]:
							python_trend["2011"] += 1
						elif "java" in item["tags"]:
							java_trend["2011"] += 1
							
					#year 2012
					
					elif (item["creation_date"] > 1325376000 and item["creation_date"] < 1356998399):
						#print("here")
						if "python" in item["tags"]:
							python_trend["2012"] += 1
						elif "java" in item["tags"]:
							java_trend["2012"] += 1
							
					#year 2013
					
					elif (item["creation_date"] > 1356998400 and item["creation_date"] < 1388534399):
						if "python" in item["tags"]:
							python_trend["2013"] += 1
						elif "java" in item["tags"]:
							java_trend["2013"] += 1
							
					#year 2014
					
					elif (item["creation_date"] > 1388534400 and item["creation_date"] < 1420070399):
						if "python" in item["tags"]:
							python_trend["2014"] += 1
						elif "java" in item["tags"]:
							java_trend["2014"] += 1
							
					#year 2015
					
					elif (item["creation_date"] > 1420070400 and item["creation_date"] < 1451606399):
						if "python" in item["tags"]:
							python_trend["2015"] += 1
						elif "java" in item["tags"]:
							java_trend["2015"] += 1
							
					#year 2016
					
					elif (item["creation_date"] > 1451606400 and item["creation_date"] < 1483228799):
						if "python" in item["tags"]:
							python_trend["2016"] += 1
						elif "java" in item["tags"]:
							java_trend["2016"] += 1
			except KeyError:
				print("")
				
			#time.sleep(0.2)
				
	print(python_trend)
	print(java_trend)
	
	dicts = python_trend, java_trend
	
	with open(r'questions\trend.csv', 'w') as ofile:
    writer = csv.writer(ofile, delimiter='\t')
    writer.writerow(['Year', 'python_trend', 'java_trend'])
    for key in python_trend.keys():
        writer.writerow([key] + [d[key] for d in dicts])
	
	return;
	
def mostPopularUnansweredQuestion():

	question_value_python = {}
	count_python = 0
	question_value_java = {}
	count_java = 0

	for filename in glob.glob(r"unansweredQuestions\*.json"):
		with open(filename, 'r') as f:
			P = json.load(f)
			
			try:
				for item in P["items"]:
					if "python" in item["tags"]:
						impact_factor = item["view_count"] + item["score"]
						question_value_python[item["title"]] = impact_factor
						count_python += 1
					elif "java" in item["tags"]:
						impact_factor = item["view_count"] + item["score"]
						question_value_java[item["title"]] = impact_factor
						count_java += 1
			except KeyError:
				print("")
				
				
	python_questions_sorted = sorted(question_value_python.items(), key=operator.itemgetter(1), reverse = True)
	java_questions_sorted = sorted(question_value_java.items(), key=operator.itemgetter(1), reverse = True)
					
	#print(count_python)
	#print(count_java)

	if(count_python > count_java):
		print("Python has more number of unanswered questions than Java")
	elif(count_java > count_python):
		print("Java has more number of unanswered questions than Python")
	else:
		print("It's difficult to tell at this point which has more number of unanswered questions")

	top_three_python = sorted(question_value_python, key=question_value_python.get, reverse=True)[0:3]

	print("\nTop three most popular unanswered questions under 'Python' tag are:")
	print("1. {val}".format(val = top_three_python[0]))
	print("2. {val}".format(val = top_three_python[1]))
	print("3. {val}".format(val = top_three_python[2]))

	top_three_java = sorted(question_value_java, key=question_value_java.get, reverse=True)[0:3]

	print("\nTop three most popular unanswered questions under 'Java' tag are:")
	print("1. {val}".format(val = top_three_java[0]))
	print("2. {val}".format(val = top_three_java[1]))
	print("3. {val}".format(val = top_three_java[2]))

	print("\nPlease open .csv file for more detailed summary")

	pyexcel.save_as(array = python_questions_sorted, dest_file_name = r'unansweredQuestions\pythonUnansweredSorted.csv')
	pyexcel.save_as(array = java_questions_sorted, dest_file_name = r'unansweredQuestions\javaUnansweredSorted.csv')
	
	return;
	
def topThreeUsersForBadges():

	bronze_list = {}
	silver_list = {}
	gold_list = {}
	displayname_list = {}

	for filename in glob.glob(r"users\*.json"):
		with open(filename, 'r') as f:
			P = json.load(f)
			
			try:
				for item in P["items"]:
					#print(item)
					bronze_list[item["user_id"]] = item["badge_counts"]["bronze"]
					silver_list[item["user_id"]] = item["badge_counts"]["silver"]
					gold_list[item["user_id"]] = item["badge_counts"]["gold"]
					displayname_list[item["user_id"]] = item["display_name"]
			except KeyError:
				print("")
			
	bronze_list_sorted = sorted(bronze_list.items(), key=operator.itemgetter(1), reverse = True)
	silver_list_sorted = sorted(silver_list.items(), key=operator.itemgetter(1), reverse = True)
	gold_list_sorted = sorted(gold_list.items(), key=operator.itemgetter(1), reverse = True)

	top_three_bronze = sorted(bronze_list, key=bronze_list.get, reverse=True)[0:3]
	top_three_silver = sorted(silver_list, key=silver_list.get, reverse=True)[0:3]
	top_three_gold = sorted(gold_list, key=gold_list.get, reverse=True)[0:3]

	print(top_three_bronze)
	print(top_three_silver)
	print(top_three_gold)

	i = 1
	top_3_bronze = []
	print("\n Top 3 users with maximum number of bronze badges are:")
	for item in top_three_bronze:
		print("\t {pos}. {val}".format(pos=i, val = displayname_list[item]))
		top_3_bronze.append(displayname_list[item])
		i += 1
		
	i = 1
	top_3_silver = []
	print("\n Top 3 users with maximum number of silver badges are:")
	for item in top_three_silver:
		print("\t {pos}. {val}".format(pos=i, val = displayname_list[item]))
		top_3_silver.append(displayname_list[item])
		i += 1
		
	i = 1
	top_3_gold = []
	print("\n Top 3 users with maximum number of gold badges are:")
	for item in top_three_gold:
		print("\t {pos}. {val}".format(pos=i, val = displayname_list[item]))
		top_3_gold.append(displayname_list[item])
		i += 1
		
	pyexcel.save_as(array = bronze_list_sorted, dest_file_name = r'users\bronzeListSorted.csv')
	pyexcel.save_as(array = silver_list_sorted, dest_file_name = r'users\silverListSorted.csv')
	pyexcel.save_as(array = gold_list_sorted, dest_file_name = r'users\goldListSorted.csv')
	pyexcel.save_as(array = top_3_bronze, dest_file_name = r'users\top_3_bronze.csv')
	pyexcel.save_as(array = top_3_silver, dest_file_name = r'users\top_3_silver.csv')
	pyexcel.save_as(array = top_3_gold, dest_file_name = r'users\top_3_gold.csv')
	
	return;
	

mostPopularBadges()
FAQsOnMostPopularTags()
comparingTrends()
mostPopularUnansweredQuestion()
topThreeUsersForBadges()