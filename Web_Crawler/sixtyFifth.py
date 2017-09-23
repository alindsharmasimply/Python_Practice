from urllib import *
from bs4 import *
import os

def create_directory(directory):
	if not os.path.exists(directory):
		print "Creating the directory"
		os.makedirs(directory)

def create_data_files(project_name, base_URL):
	queue = os.path.join(project_name, 'queue.txt')
	crawled = os.path.join(project_name, 'crawled.txt')
	if not os.path.isfile(queue):
		write_data(queue, base_URL)
	if not os.path.isfile(crawled):
		write_data(crawled,'')

def write_data(path, data):
	with open(path, 'w') as fp:
		fp.write(data)
		fp.close()

def append_data(path, data):
	with open(path,'a') as fp:
		fp.write(data,'\n')
		fp.close()

def delete_data(path):
	with open(path,'w') as fp:
		fp.write('')
		fp.close()

def file_to_set(file_name):
	result = set()
	with open(file_name, 'rt') as fp:
		for line in fp:
			result.add(line.replace('\n',''))
	return result

def set_to_file(links, file_name):
	with open(file_name, 'w') as fp:
		for l in sorted(links):
			fp.write(l + '\n')
