*** Test Cases ***

Create And Log A List
    @{my_list}=    Create List    Apple    banana    kivi
    Log    ${my_list}


Loop Through List
    @{fruits}=    Create List    apple    banana    orange
    FOR     ${fruits}    IN    @{fruits}
    Log    I like ${fruits}
        
    END
       


Check If Mango Is In The List
    @{fruits}=    Create List    Apple    kivi    dragonFruit
    ${is_apple}=    Evaluate    'Apple' in ${fruits}
    Run Keyword If    ${is_apple}    Log    Apple is in ${fruits}
    

Count Items In List
    @{fruits}=    Create List    apple    banana    orange
    ${count}=    Get Length    ${fruits}
    Log    there are ${count} fruits in a list
    