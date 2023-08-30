sec=int(input("enter the number of sec:"))
hour=sec//3600
minutes=(sec%3600)//60
second=sec%60
print(hour,"hours",minutes,"minutes",second,"seconds")
