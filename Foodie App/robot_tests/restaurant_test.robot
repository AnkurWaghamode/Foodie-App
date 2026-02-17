*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    BuiltIn

*** Variables ***
${BASE_URL}    http://127.0.0.1:5000

*** Test Cases ***
Create Restaurant
    Create Session    foodie    ${BASE_URL}
    ${random}=    Evaluate    random.randint(1,10000)    random
    ${payload}=    Create Dictionary
    ...    name=Robot Hotel ${random}
    ...    category=Chinese
    ...    location=Delhi
    ...    contact=8888888888

    ${response}=    POST On Session    foodie    /api/v1/restaurants    json=${payload}

    Should Be Equal As Integers    ${response.status_code}    201
