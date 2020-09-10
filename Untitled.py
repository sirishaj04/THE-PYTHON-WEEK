#!/usr/bin/env python
# coding: utf-8

# In[1]:


lst1=list(map(int,(input("enter list: ").split(" "))))
lst2=list(map(int,(input("enter list: ").split(" "))))
i=0
w=[]
p=0
def listcheck(lst2):

    if len(lst2)==0:

        return 0
    else:

        return 1

length=len(lst1)

while i<length:
    if listcheck(lst2):
        for j in lst2:
            if lst1[i]==j:
                index=lst2.index(j)
                p=lst2.pop(index)
                #print(lst2)
                w.append(p)
                #print(w)
                i=i+1
                break
            else:
                index=lst2.index(j)
                del lst2[index]
                #print(lst2)
                break
    else:
        break


#print(w)
#print(lst2)
if w==lst1:
    print("IT's a Match")
else:
    print("It's Gone")
    


# In[2]:


lst1=list(map(int,(input("enter list: ").split(" "))))
lst2=list(map(int,(input("enter list: ").split(" "))))
i=0
w=[]
p=0
def listcheck(lst2):

    if len(lst2)==0:

        return 0
    else:

        return 1

length=len(lst1)

while i<length:
    if listcheck(lst2):
        for j in lst2:
            if lst1[i]==j:
                index=lst2.index(j)
                p=lst2.pop(index)
                #print(lst2)
                w.append(p)
                #print(w)
                i=i+1
                break
            else:
                index=lst2.index(j)
                del lst2[index]
                #print(lst2)
                break
    else:
        break


#print(w)
#print(lst2)
if w==lst1:
    print("IT's a Match")
else:
    print("It's Gone")


# In[ ]:




