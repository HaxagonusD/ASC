from random import * 

#This program is supposed to give you random results in a sentence from these lists

cities = ["Philadelphia", "Boston", "New York City"] 
subjects = ["Hard Science", "Social Science", "Science"] 
jobs = ["Science", "Engineer", "Doctor"]


citiesInput = raw_input("Where will you live?")
cities.append(citiesInput)

subjectsInput = raw_input("What subject will you studie?")
subjects.append(subjectsInput)

jobsInput = raw_input("What job will you have?")
jobs.append(jobsInput)