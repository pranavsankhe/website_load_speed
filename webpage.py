from urllib.request import urlopen 
import time 

''' get the load time of a website'''
def download_webpage():
	url = input("Feed me the website name to chew on: ")
	#url = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'
	respones = urlopen(url, timeout = 60)
	return respones.read()

def calc_time():
	t0 = time.time()
	file = download_webpage()
	t1 = time.time()
	print("Time taken to load: {}".format(t1-t0))

calc_time()

