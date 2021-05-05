

r = [1,2]
s=[1,2,3,4,5]

for film in s:
    for rec in r:
        if(film == rec):
            print(rec)
            print(film)
            s.pop(film)
print(s)
