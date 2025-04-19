*** Settings ***
Library    OperatingSystem



*** Test Case ***
Check File Exists
    [Documentation]     Verify file  presence
    File Should Exist    myfile.txt