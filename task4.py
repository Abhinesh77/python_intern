#list
a=[1,2,3,4]
for x in a:
    print(x,end="");
print("")    
    
a.append(5);
for x in a:
    print(x,end="");
print("")    
    
a.remove(2);
for x in a:
    print(x,end="");
print("")

max=max(a);
min=min(a);
print("largest element is",max);
print("smallest element is",min);
#tuple
b=(6,7,8,9,10);
print(b[::-1])
c=("a","b","c","d");
d=list(c)
print(d)
    
