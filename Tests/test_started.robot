*** Variables ***
| ${BROWSER} | firefox
| ${ROOT}    | https://dev.fitbit.com/
${tab_options}  Getting Started   Build   Manage  Community

*** Settings ***
| Library    | SeleniumLibrary
| Library    | PageObjectLibrary
|
| Suite Setup    | Open browser | ${ROOT} | ${BROWSER}
| Suite Teardown | Close all browsers
#Library     SeleniumLibrary
Library     GuidesPage.GuidesPage
#Library     StartedPage.StartedPage

*** Test Cases ***
| Verify details of getting started page
| | [Documentation] | Go to getting started page and verify details on the page
| | [Setup]         | Go to page | StartedPage
| |
| | verify started page
| | verify tab options | ${tab_options}
| |
| Verify that user can search and is redirected to the page
| | [Documentation] | Verify that user can search and is redirected to the page
| |
| | [Setup]         | Go to page | StartedPage
| | verify goto guides page

