import io
import os
import os.path
import json
import argparse
from pyhunter import PyHunter

parser = argparse.ArgumentParser()
parser.add_argument("-fns",help="Find names based on domain and persons name.",action="store_true")
parser.add_argument("-fnm",help="Find multiple names based on domain and persons name.",action="store_true")
parser.add_argument("-fe",help="Find all email addresses associated with all domains in a text file",action="store_true")
parser.add_argument("-v",help="Verify an email address",action="store_true")
parser.add_argument("-c",help="Check how many calls left",action="store_true")
args=parser.parse_args()


hunter = PyHunter('b2052e9761534c20476af9ead613ab66de90b615')
results = hunter.domain_search('rigidbits.com')


if (args.fe):
	infile = input("Location of URLs file..")
	outfile = input("Location of output text file..")
	fopen = open(outfile, 'w')
	with open(infile) as f:
	    for i in f:
	        x = i.rstrip('\n')
	        url = x
	        print(url)
	        results = hunter.domain_search(url)
	        printed = json.dumps(results)
	        fopen.write(printed)
	fopen.close()
elif (args.fns):
	company1 = input("Enter company of interest..")
	name = input("Enter person of interest")
	results = hunter.email_finder(company=company1, full_name=name, raw=True)
	print(results)
elif (args.v):
	validatepls = input("File with Email addresses to validate..")
	outfile = input("Location of output text file..")
	fopen = open(outfile, 'w')
	with open(validatepls) as f:
	    for i in f:
	        x = i.rstrip('\n')
	        print(x)
	        emailname = x 
	        print(emailname)
	        validated = hunter.email_verifier(emailname)
	        printed = json.dumps(validated)
	        fopen.write(emailname)
	        fopen.write('\n')
	        fopen.write(printed)
	fopen.close()
elif (args.c):
	number_left = hunter.account_information()
	print(number_left)

	


