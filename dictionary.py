# Restructuring the company data: Suppose you have a dictionary that contains information about employees at a company. Each employee is identified by an ID number, and their information includes their name, department, and salary. You want to create a nested dictionary that groups employees by department so that you can easily see the names and salaries of all employees in each department.
# Write a Python program that when given a dictionary, employees, outputs a nested dictionary, dept_employees, which groups employees by department.
def group_employees_by_department( employees ):
    dept_employees = {}

    for emp_id, emp_info in employees.items():
        dept = emp_info['department']
        name = emp_info['name']
        salary = emp_info['salary']

        if dept not in dept_employees:
            dept_employees[dept] = {}

        dept_employees[dept][name] = salary

    return dept_employees


if __name__ == "__main__":
    employees = {
        101: {'name': 'Alice Johnson', 'department': 'Engineering', 'salary': 75000},
        102: {'name': 'Bob Smith', 'department': 'Marketing', 'salary': 65000},
        103: {'name': 'Charlie Brown', 'department': 'Engineering', 'salary': 80000},
        104: {'name': 'Diana Prince', 'department': 'HR', 'salary': 60000},
        105: {'name': 'Eve Adams', 'department': 'Marketing', 'salary': 70000},
        106: {'name': 'Frank Miller', 'department': 'Engineering', 'salary': 85000}
    }

    dept_employees = group_employees_by_department(employees)

    print("Employees grouped by department:")
    for department, employees_in_dept in dept_employees.items():
        print(f"\n{department}:")
        for name, salary in employees_in_dept.items():
            print(f"  {name}: ${salary}")
