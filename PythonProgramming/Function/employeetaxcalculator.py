def calculate_employee_net_salary(name, age, gender, pan_no, salary):
    """
    Calculate the net salary of an employee after applying tax, if their salary is greater than $80,000.
    Also returns employee details.

    Parameters:
    - name: String, the name of the employee.
    - age: Integer, the age of the employee.
    - gender: String, the gender of the employee.
    - pan_no: String, the Permanent Account Number (PAN) of the employee.
    - salary: Float, the current salary of the employee.

    Returns:
    - A dictionary containing the employee's details and their net salary after tax if applicable.
    """
    if 80000 < salary <= 100000:
        tax_rate = 0.20  # 20% tax rate
    elif salary > 100000:
        tax_rate = 0.25  # 25% tax rate
    else:
        tax_rate = 0.0  # No tax

    # Calculate the tax amount
    tax_amount = salary * tax_rate
    # Calculate the net salary
    net_salary = salary - tax_amount

    # Return employee details along with the net salary
    return {
        "Name": name,
        "Age": age,
        "Gender": gender,
        "PAN No": pan_no,
        "Original Salary": salary,
        "Net Salary": net_salary
    }

# Example usage
name = str(input("Please enter the name of employee"))
print(name)
employee_details = calculate_employee_net_salary("John Doe", 35, "Male", "ABCDE1234F", 95000)
for key, value in employee_details.items():
    if isinstance(value, float):
        print(f"{key}: ${value:.2f}")
    else:
        print(f"{key}: {value}")
