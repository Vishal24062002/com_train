*** Settings ***
Library    BuiltIn
Library    Collections

*** Test Cases ***
Add And Remove Items In List
    @{fruits}=    Create List    apple    banana
    Log    Original list: ${fruits}

    # add items
    Append To List    ${fruits}    Mango
    Append To List    ${fruits}    anguur
    Log    after adding:${fruits}

    # remove item,

    Remove From List    ${fruits}    0

    Log    after removing indexd 1(banana):${fruits}


Check Fruit Availability
    ${my_fruit}=    Set Variable    Banana
    @{fruits}=    Create List    Apple    Banana    Mango
 
    Run Keyword If    '${my_fruit}' in ${fruits}    Log    ${my_fruit} is available
    Run Keyword Unless    '${my_fruit}' in ${fruits}    Log    ${my_fruit} is NOT available

Filter List Items Starting With A
    @{fruits}=    Create List    Apple    Banana    Apricot    Mango
    @{filtered}=    Create List
 
    FOR    ${fruit}    IN    @{fruits}
        Run Keyword If    '${fruit}'[0]=='A'    Append To List    ${filtered}    ${fruit}
    END
    

  