*** Settings ***
Library           OperatingSystem
Library           Collections
Library           Process

*** Variables ***
${PYTHON_CMD}     ./venv/bin/python3
${MAIN_SCRIPT}    main.py
${OUTPUT_DIR}     output

*** Test Cases ***
Generate 5 Files And Verify
    [Documentation]    Runs main.py to generate 5 files and verifies count and uniqueness.
    
    # Run the python script
    ${result}=    Run Process    ${PYTHON_CMD}    ${MAIN_SCRIPT}    -n    5    cwd=${CURDIR}/..
    Should Be Equal As Integers    ${result.rc}    0
    Log    ${result.stdout}
    
    # Count generated files
    ${file_count}=    Get File Count Recursive    ${CURDIR}/../${OUTPUT_DIR}
    Should Be Equal As Integers    ${file_count}    5
    
    # Verify Content Uniqueness
    Verify Files Content Uniqueness    ${CURDIR}/../${OUTPUT_DIR}

*** Keywords ***
Get File Count Recursive
    [Arguments]    ${path}
    ${count}=    Run Process    find    ${path}    -type    f    -name    *.txt    stdout=PIPE
    # Count lines in stdout
    ${lines}=    Get Line Count    ${count.stdout}
    RETURN    ${lines}

Verify Files Content Uniqueness
    [Arguments]    ${path}
    # Get all file paths
    ${find_result}=    Run Process    find    ${path}    -type    f    -name    *.txt    stdout=PIPE
    @{file_paths}=    Split String    ${find_result.stdout}
    
    ${contents}=    Create List
    
    FOR    ${file_path}    IN    @{file_paths}
        Continue For Loop If    '${file_path}' == ''
        ${content}=    Get File    ${file_path}
        Append To List    ${contents}    ${content}
    END
    
    ${count}=    Get Length    ${contents}
    # Convert list to set (remove duplicates) - Robot doesn't have direct Set conversion in built-in
    # Use Remove Duplicates from Collections library
    ${unique_contents}=    Copy List    ${contents}
    Remove Duplicates    ${unique_contents}
    ${unique_count}=    Get Length    ${unique_contents}
    
    Should Be Equal As Integers    ${count}    ${unique_count}    msg=Found duplicate file contents!

*** Keywords ***
# Helper to count lines since String library might be needed
    
*** Settings ***
Library    String
