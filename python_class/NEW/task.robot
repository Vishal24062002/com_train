*** Settings ***
Library           Collections

*** Test Cases ***
Creating a dictionary and Logging it
   @{my_dict}=    Create Dictionary    name = Vishal    age = 22    gender = Male
    Log    ${my_dict}
    
    Set To Dictionary    ${my_dict}     clas    12
    Log    after adding    ${my_dict}    

