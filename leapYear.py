year = int(input("Enter a year: "))
mounth = int(input("Enter a mounth 1-12:"))

def isYearLeap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def daysInMonth(year,month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and isYearLeap(year):
		res = 29
	return res

print("The year",year,"is a leap year ?",isYearLeap(year))
print("In the mouth",mounth,"had",daysInMonth(year,mounth),"days")

