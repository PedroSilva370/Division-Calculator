# Division Calculator with Exception Handling

## Description
This project is a basic Python program that performs a division between two values provided by the user. It demonstrates how to handle common runtime errors using Python's exception handling structure.

## Objective
- Prompt the user to enter two integer values  
- Perform the division  
- Handle errors such as division by zero and invalid input  
- Display the result if no error occurs  

## Requirements
- Use `try`, `except`, and `else`  
- Handle `ZeroDivisionError`  
- Handle `ValueError`  

## How It Works
1. The program asks the user for two values  
2. It converts the inputs to integers  
3. It attempts to perform the division  
4. If an error occurs, an appropriate message is displayed  
5. If no error occurs, the result is printed  

## Example
first value: 10  
second value: 0  
Error: cannot divide by zero.  

first value: 10  
second value: 2  
Result: 5.0  

## Notes
- Only integer values are accepted  
- Invalid inputs will trigger an error message  
- Exception handling prevents the program from crashing  

## Possible Improvements
- Support floating-point numbers  
- Add a loop to repeat the operation  
- Improve input validation  

## Author
Pedro Gaudencio
