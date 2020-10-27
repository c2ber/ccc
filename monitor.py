#-*- coding:utf-8 -*-
import sys
import os
import datetime
from time import sleep
import shutil


### path
pcap_path = "./"
accesslog_path = "/server/logs/access.log"


### By G
file_list = os.listdir(pcap_path)
file_list_py = [file for file in file_list if file.endswith(".pcapng")]

def tmp_dir():
	try:
		if not(os.path.isdir('tmp')):
			os.makedirs(os.path.join('tmp'))
	except OSError as e:
		if e.errno != errno.EEXIST:
			print("Failed to create directory!!!!!")
			raise

while 1:	

	lambda: os.system('cls')

	print("################################### pcap - http.request")
	if file_list_py is not None:
		tmp_dir()
		for line in file_list_py:
			os.system('tshark -r %s -Y http.request -o data.show_as_text:TRUE -T fields -e frame.time -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e http.request.method -e http.request.full_uri -e http.user_agent -e text >> request.txt ' %line )
			shutil.move(line, 'tmp/'+line)

		with open('request.txt', 'r') as f:
			for line in f.readlines()[0:10:-1]:
				print(line.strip())
		f.close()


	else:
		with open('request.txt', 'r') as f:
			for line in f.readlines()[0:10:-1]:
				print(line.strip())
		f.close()


	print("################################### accesslog")
	with open(accesslog_path, 'r') as f:
		for line in f.readlines()[0:10:-1]: 
			print(line.strip())
	f.close()

	time = datetime.datetime.now()
	print("############################# end time = " + str(time))

	sleep(60)

