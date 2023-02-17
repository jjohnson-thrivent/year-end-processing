import os
import datetime
from datetime import datetime
import logging
logging.basicConfig( filename = 'year_end_move.log',
encoding = "utf-8", level = logging.INFO )


def scan(source_dir):
	'''
	This function takes in a source directory
        and yields a list of files in that directory
	'''
	try:
		logging.info("Scanning for files in:  " + source_dir + "\n")
		for root, dirs, files in os.walk(source_dir):
	        	return files
	except Exception as e:
		logging.error(e)


def move(source_file, dest_file):
	'''
	This function takes in a source file moves it to a destination.
	 A directory and filename must be given for source and destination
	'''
	try:
		os.rename(source_file, dest_file)
		logging.info(source_file + " has been moved to: " + dest_file + "\n")
	except Exception as e:
		logging.error(e)


if __name__ == "__main__":
	try:
		# Getting date
	    now = datetime.now()
	    dt_string = now.strftime("%Y%m%d_%H%M%S")
	    # Setting variables
	    batch_dir = "/usr/local/inet/shared/fraternal/tchoice/batch/"
	    source_dir = batch_dir + "input/"
	    file_types = ['thriventchoice_combine_delete',
            'thriventchoice_member_annual_elig']
        # Scan import directory files yearly files
	    # Scanning directory for files
	    output = scan(source_dir)
	    output2 = scan(batch_dir + "Yearly_Eligibility_Files/")
	    trigger = 0
	    for item in output:
	    	if item.startswith('thriventchoice_member_annual_elig'):
	    		trigger = 1
	    for item in output2:
	    	if item.startswith('thriventchoice_member_annual_elig'):
	    		trigger = 1	    		
	    if trigger == 1:
			logging.info(source_file + "Found a Yearly Eligibility File, moving files.")
		    # Looping through file file_types
			for file_type in file_types:
		    	# Comparing the files to the file types
		    	for file in output:
				if file.startswith(file_type):
					# Moving the files
					source_file = source_dir + file
					if file_type == 'thriventchoice_combine_delete':
						dest_dir = batch_dir + "CombineDeleteHoldYEP/"
						dest_file = dest_dir + file_type + "_" + dt_string + ".csv"
						move(source_file, dest_file)
					if file_type == 'thriventchoice_member_annual_elig':
						dest_dir = batch_dir + "Yearly_Eligibility_Files/"
						dest_file = dest_dir + file
						move(source_file, dest_file)
        except Exception as e:
            logging.error(e)
 
