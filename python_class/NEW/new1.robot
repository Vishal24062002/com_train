*** Settings ***
Documentation    validate a login form
Library    SeleniumLibrary
Test Setup    open the browser with saucedemo 
Test Teardown    Close Browser

Resource    resource.robot
Resource    six.robot

# *** Test Cases ***
# validate unsucessfull login
#     fill the login form
    
#     wait until it checks and display error message

# *** Keywords ***
# fill the login form
#     Input Text   user-name    ${user_name}
#     Input Password    password    ${invalid_password}
    
#     Click Button    login-button

# wait until it checks and display error message
#     Wait Until Element Is Visible    xpath://*[@id="login_button_container"]/div/form/div[3]/h3

*** Test Cases ***
validate cards display in shopping page
    fill the login form    ${user_name}    ${valid_password}
    wait till a element is visible    xpath://*[@id="shopping_cart_container"]/a


*** Keywords ***


Fill The Login Form
    [Arguments]    ${username}    ${password}
    Input Text    user-name    ${username}
    Input Password    password    ${password}
    Click Button    login-button


wait till a element is visible
    [Arguments]    ${element}
    wait till a element is visible    ${element}
    

