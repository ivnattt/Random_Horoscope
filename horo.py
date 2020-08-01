import random
a=['Today is a lucky day for you', 'You know you are kind at heart', 'It is hard being nice to people given the circumstances', 'You tend to mind your own buiness']


s=[]

for _ in range(3):
    k=random.randint(0,3)
    l=a[k]
    s.append(l)

print('. '.join(s))



    
