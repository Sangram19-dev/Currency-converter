#currency converter

with open("currency.txt") as f:
    a=f.readlines()

#print(a)
currDict={}
for line in a:
    parsed=line.split("\t")
    currDict[parsed[0]]=parsed[1]
    #print(parsed)
    #break
#print(currDict)
amount=int(input("Enter your amount: \n"))
print("Enter the name of currency you want to convert this amount to? Availavle option\n")
[print(item) for item in currDict.keys()]
cur=input("please enter one of this value:\n")
print(f"{amount} INR is Equal to {amount * float(currDict[cur])} {cur}")