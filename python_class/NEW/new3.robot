*** Settings ***
Library    SSHLibrary

*** Variables ***
${host}    test.rebex.net
${USERNAME}    demo
${PASSWORD}    password
${port}    22

*** Test Cases ***
connect and run command
    Open Connection    ${host}    ${port}
    Set Client Configuration    timeout=30s
    Login    ${USERNAME}    ${PASSWORD}
    ${output}=    Execute Command    ls
    Log    ${output}
    Close Connection
   