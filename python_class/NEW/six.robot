*** Settings ***

Documentation    To validate a login form

Library    SeleniumLibrary

*** Test Cases ***
validate unsuccessfully login
    open the browser with sacedemo
    fill the login form
    wait until it checks and display error message
    verify error message is correct

*** Keywords ***
open the browser with sacedemo
    Open Browser    https://www.saucedemo.com/    chrome    

fill the login form
    Input Text    user-name    standard_user
    Input Password    password    secret_sauce123
    Click Button    login-button

wait until it checks and display error message
    Wait Until Element Is Visible    xpath://*[@id="login_button_container"]/div/form/div[3]/h3

verify error message is correct    
    ${result}    Get Text    xpath://*[@id="login_button_container"]/div/form/div[3]/h3
    Should Be Equal As Strings    ${result}    Epic sadface: Username and password do not match any user in this service 