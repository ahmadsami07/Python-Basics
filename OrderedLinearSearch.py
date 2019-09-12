#Ordered Linear Search

def orderedlinearsearch(testlist,target):
  pos=0
  notfound=True
  stop=False
  found=False

  while pos<len(testlist) and not stop and notfound:
    if testlist[pos]==target:
      found=True
      stop=True
    elif testlist[pos]>target:
      stop=True
    else:
      pos=pos+1
        
  return found



alist=[1,3,4,5,6,7,9,10,45,66]

item=int(input("Select target ASAP."))

orderedlinearsearch(alist,item)