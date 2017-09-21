try:
	def function1(a, b):
		print a / b
	function1(20 / 0)
except Exception as e:
	print e
finally:
	print "This will be printed no matter what"