import calendar

def magic(k,mm,yy):
	mag = k*mm
	if mag == (yy % 100):
		print k, mm, yy

def main():
	yy = 2000
	mm = 1
	while yy < 3000:
		(a,b) = calendar.monthrange(yy, mm)
		k = 1
		while mm <= 12:
			
			while k <= b:
				magic(k,mm,yy),
				k += 1
			mm += 1
			k = 1
		mm = 1
		yy += 1
main()