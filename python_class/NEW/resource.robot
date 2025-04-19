*** Settings ***

Documentation    a resource file to reuse the keyword and variable 
Library    SeleniumLibrary

*** Variables ***

${user_name}    standard_user
${valid_password}    secret_sauce
${invalid_password}    secret_sauce123

*** Keywords ***

open the browser with saucedemo

    Open Browser    https://www.saucedemo.com/    chrome