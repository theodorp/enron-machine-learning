#!/usr/bin/python

""" 
    starter code for exploring the Enron dataset (emails + finances) 
    loads up the dataset (pickled dict of dicts)

    the dataset has the form
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person
    you should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

# print "Data points in enron_data:", len(enron_data)
# print "Number of features per person:", len(enron_data.values()[1])
# print "Number of POIs in dataset:", sum([enron_data[name]['poi'] for name in enron_data.keys()])
# print "Total value of stock belonging to James Prentice:", enron_data['PRENTICE JAMES']['total_stock_value']
# print "Number of emails from Wesley Colwell to a POI:", enron_data['COLWELL WESLEY']['from_this_person_to_poi']
# print "Total exercised stock options of Jeff Skilling:", enron_data['SKILLING JEFFREY K']['exercised_stock_options']

# print "Money taken home from Lay, Skilling, Fastow:", \
	# enron_data['LAY KENNETH L']['total_payments'], \
	# enron_data['SKILLING JEFFREY K']['total_payments'], \
	# enron_data['FASTOW ANDREW S']['total_payments']

# print "Number of people in dataset with quantifited salary:", \
	# len([enron_data[name]['salary'] for name in enron_data.keys() if enron_data[name]['salary'] != 'NaN'])

# print "Number of people in dataset with quantifited email adresses:", \
	# len([enron_data[name]['email_address'] for name in enron_data.keys() if enron_data[name]['email_address'] != 'NaN'])

## May have sacrificed reability here... 
# print "Number of people in dataset with NaN as total payments (%):", \
	# (len([enron_data[name]['total_payments'] for name in enron_data.keys() \
		# if enron_data[name]['total_payments'] == 'NaN' and enron_data[name]['poi'] == True]))/float((len(enron_data)))

	