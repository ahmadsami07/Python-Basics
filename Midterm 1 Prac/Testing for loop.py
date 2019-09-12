letter="magalal"

length=len(letter)

for i in range(-1,-length-1,-1):
    print(letter[i])
    
prefixes="JKLMNOPQ"
length=len(prefixes)
suffixes="ack"

for i in range(length):
    name=(prefixes[i]+suffixes)
    if name=="Oack" or name=="Qack":
        print(name.replace("ac","uac"))
    else:
        print(prefixes[i]+suffixes)
    