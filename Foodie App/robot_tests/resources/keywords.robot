*** Settings ***
Library    RequestsLibrary
Library    Collections
Resource   variables.robot

*** Keywords ***
Create API Session
    Create Session    foodie    ${BASE_URL}

Create Restaurant
    [Arguments]    ${name}    ${category}    ${location}    ${contact}
    ${payload}=    Create Dictionary
    ...    name=${name}
    ...    category=${category}
    ...    location=${location}
    ...    contact=${contact}

    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${payload}
    RETURN    ${response}

Create User
    [Arguments]    ${name}    ${email}    ${password}
    ${payload}=    Create Dictionary
    ...    name=${name}
    ...    email=${email}
    ...    password=${password}

    ${response}=    POST On Session    foodie    /api/v1/users    json=${payload}
    RETURN    ${response}
