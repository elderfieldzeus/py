dist = float(input("Enter distance in km: "))

a = float(input("Enter fuel for Car A in L: "))
b = float(input("Enter fuel for Car B in L: "))

if a == b:
	print("Both cars have the same efficiency")
elif a < b:
	print("Car A is more efficient by {:.2f}%".format((b - a) / a * 100))
else:
	print("Car B is more efficient by {:.2f}%".format((a - b) / b * 100))