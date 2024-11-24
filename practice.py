"""
for x in range (10,101,10):
    print(x)
else:
  print("Looop Finished")

list=[25,30,50,70,80]

for x in list: 
   
    if(x==30) :
        continue  # Will not continue further iteration and move to next iteration
    print(x)
"""


for x in range(0,5):
    for y in range(x):
        print(y,end="")  
    print()

for x in range(0,3,1):
    print(x,end="")