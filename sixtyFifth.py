import os
from urllib import *
from bs4 import *


def createProjectDirectory(directory):
	if not os.path.exists(directory):
		print "Creating the directory ", directory
		os.makedirs(directory)
	else:
		print "The directory already exists"

def createDataFiles(directory, base_URL):
	queue = os.path.join(directory, 'queue.txt')
	crawled = os.path.join(directory, 'crawled.txt')
	if not os.path.isfile(queue):
		write_file(queue, base_URL)
	if not os.path.isfile(crawled):
		write_file(crawled, '')

def write_file(path, data):
	with open(path, 'w') as f:
		f.write(data)

def append_to_file(path , data):
	with open(path,'a') as f:
		f.write(data,'\n')

def delete_file_contents(path):
	open(path, 'w').close()