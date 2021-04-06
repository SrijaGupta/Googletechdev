'''
3
Sam 2223453456
Dave 4445556789
raziya 4446789999
Sam
david
raziya
'''



lines = []
phonebook ={}
d=""
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
entries=int(lines[0])
for i in range(1,entries+1):
    d=lines[i].split()
    phonebook[d[0]]=d[1]
f=0
for j in range(entries+1,len(lines)):
    for key, value in phonebook.items():
        if(key==lines[j]):
            print(key+"="+phonebook.get(key))
            f=1
            break
    if f==0:
      print("Not Found")
    f=0
                    
