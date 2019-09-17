*** Variables ***
| ${BROWSER} | firefox
| ${ROOT}    | https://the-internet.herokuapp.com/

*** Settings ***
| Library    | SeleniumLibrary
| Library    | PageObjectLibrary
|
| Suite Setup    | Open browser | ${ROOT} | ${BROWSER}
| Suite Teardown | Close all browsers


*** Test Cases ***
| Valid Login
| | [Documentation] | Verify that we can successfully log in to the internet
| | [Setup]         | Go to page | LoginPage
| | 
| | Enter username | tomsmith
| | Enter password | SuperSecretPassword!
| | Click the login button
| | The current page should be | SecureAreaPage