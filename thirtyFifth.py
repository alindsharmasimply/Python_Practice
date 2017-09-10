import math
class Complex():
	"""docstring for Complex"""
	def __init__(self, real, imag):
		self.__real = real
		self.__imag = imag
	def getReal(self):
		return self.__real
	def getImag(self):
		return self.__imag
	def setReal(self, val):
		if type(val) not in (int,float):
			raise Exception ('real values')
		self.__real = val
	def setImag(self, val):
		self.__imag = val
	def mod(self):
		return math.sqrt(self.getReal() ** 2 + self.getImag() ** 2)
c = Complex(0, 0)
c.setReal(1)
c.setImag(1)
print c.mod()