matn = input()
belgi = input()
if belgi in matn:
    print(matn.find(belgi) - 1)
else:
    print(-1)