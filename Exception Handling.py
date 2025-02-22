try:
    num = int(input("Enter a number: "))  
    result =  num / 10 
    print("Result:", result)

except ValueError:
    print("Error: Please enter a valid integer.")

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

except Exception as e:
    print("An unexpected error occurred:", e)

finally:
    print("Execution completed.")
