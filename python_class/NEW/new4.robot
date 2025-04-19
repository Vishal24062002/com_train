*** Settings ***
Library    SSHLibrary

*** Variables ***
${host}    test.rebex.net
${USERNAME}    demo
${PASSWORD}    password
${local_file}    sample.txt
${remote_path}    sample.txt

*** Test Cases ***
Upload File To Server
    Open Connection    ${host}
    Login    ${USERNAME}    ${PASSWORD}
    Put File    ${local_file}    ${remote_path}
    Close Connection