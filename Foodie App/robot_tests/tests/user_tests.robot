*** Settings ***
Library    RequestsLibrary
Library    Collections

Suite Setup       Create Session    foodie    http://127.0.0.1:5000
Suite Teardown    Delete All Sessions

*** Test Cases ***
Register User Successfully
    ${payload}=    Create Dictionary
    ...    name=RobotUser
    ...    email=robotuser${TEST NAME}@gmail.com
    ...    password=1234

    ${response}=    POST On Session    foodie    /api/v1/users/register    json=${payload}

    Should Be Equal As Integers    ${response.status_code}    201
