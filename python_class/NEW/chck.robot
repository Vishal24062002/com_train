# *** Settings ***
# Library    BuiltIn

# *** Variables ***
# ${NUMBER}    42

# *** Test Cases ***
# Check Type Of Integer
#     ${result}=    Evaluate    isinstance(${NUMBER}, int)
#     Should Be True    ${result}


*** Test Cases ***

check Variable Types
    ${number}=    Set Variable    1234
    ${text}=    Set Variable    hello
    ${list}=    Set Variable    1    2    3
    ${dict}=    Set Variable    name=john    age=30

    ${number_type}=    Evaluate    type(${number}).__name__
    ${text_type}=    Evaluate    type('${text}').__name__
    ${list_type}=    Evaluate    type(${list}).__name__
    ${dict_type}=    Evaluate    type(${dict}).__name__

    Log     Number type:${number_type}
    Log     Text type:${text_type}
    Log     List type:${list_type}
    Log     Dict type:${dict_type}

