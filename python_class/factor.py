import csv
li=[{'name':'vishal','age':'10','city': 'new york'},
    {'name':'vishal','age':'10','city': 'new york'},
    {'name':'vishal','age':'10','city': 'new york'},
    {'name':'vishal','age':'10','city': 'new york'},
    {'name':'vishal','age':'10','city': 'new york'},
    {'name':'vishal','age':'10','city': 'new york'}
    ]
with open('people.csv','w',newline='')as w:
    writer=csv.DictWriter(w,fieldnames=['name','age','city'])
    writer.writeheader()
    
    writer.writerows(li)

