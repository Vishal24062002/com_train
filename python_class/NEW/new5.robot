*** Settings ***
Library    SSHLibrary
 
*** Variables ***
${host}    test.rebex.net
${USERNAME}    demo
${PASSWORD}    password
${REMOTE_FILE}    /readme.txt
${LOCAL_PATH}    download_readme.txt

*** Test Cases ***
Download File From Server
    Open Connection    ${host}
    Login    ${USERNAME}    ${PASSWORD}
    Get File    ${REMOTE_FILE}    ${LOCAL_PATH}
    Close Connection    