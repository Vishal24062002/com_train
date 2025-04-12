import csv
fei=['name','branch','year','cgpa']
rows=[['nikhil','coe','2','9.0'],
      ['vishal','cos','2','9.0'],
      ['prince','coe','2','9.0'],
      ['seenu','coe','2','9.0'],
      ['nikhil','coe','2','9.0'],
      
      ]

with open('test.csv','w')as csvfile:
    csvwriter = csv.writer(csvfile,dialect='excel')
    csvwriter.writerow(fei)
    csvwriter.writerows(rows)
    