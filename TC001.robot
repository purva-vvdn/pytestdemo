*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${BROWSER}  chrome
${URL}  http://172.24.131.223/code-editor

*** Test Cases ***
TC001 OPEN Browser
  OPEN BROWSER  ${URL}  ${BROWSER}  

