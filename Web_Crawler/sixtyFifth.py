from urllib import *
from bs4 import *
import os

def createProjectDirectory(directory):
	if not os.path.exists(directory):
		print "Creating the directory ", directory
		os.makedirs(directory)

createProjectDirectory('Web_Crawler')