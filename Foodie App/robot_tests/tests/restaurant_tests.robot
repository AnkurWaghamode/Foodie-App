*** Settings ***
Resource    ../resources/keywords.robot
Resource    ../data/restaurant_data.robot

Suite Setup       Create API Session
Suite Teardown    Delete All Sessions

*** Test Cases ***
Create Multiple Restaurants (Data Driven)
    FOR    ${name}    ${category}    ${location}    ${contact}    IN    @{RESTAURANTS}
        ${response}=    Create Restaurant    ${name}    ${category}    ${location}    ${contact}
        Should Be Equal As Integers    ${response.status_code}    201
    END
