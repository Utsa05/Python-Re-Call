"""
Application controller for the employee system.
"""

from developer import Developer
from employee import Employee
from manager import Manager


class EmployeeController:
    """
    Coordinate employee-related operations.
    """

    def __init__(self) -> None:
        """Initialize the controller."""

        self.employees: list[Employee] = []

    def add_employee(
        self,
        employee: Employee,
    ) -> None:
        """
        Add an employee to the system.

        Args:
            employee: Employee object.

        Raises:
            TypeError: If the object is not an Employee.
        """

        if not isinstance(employee, Employee):
            raise TypeError(
                "employee must be an Employee object."
            )

        self.employees.append(employee)

    def show_employees(self) -> None:
        """Display all employees."""

        if not self.employees:
            print("No employees found.")
            return

        for employee in self.employees:
            print(employee)
            print("-" * 40)

    def show_employee_details(
        self,
        employee: Employee,
    ) -> None:
        """
        Display employee details.

        Args:
            employee: Employee object.
        """

        print(employee.get_details())
        print(f"Work: {employee.work()}")
        print(
            f"Annual bonus: "
            f"${employee.calculate_annual_bonus():,.2f}"
        )

        if isinstance(employee, Developer):
            print(employee.write_code())

        elif isinstance(employee, Manager):
            print(employee.manage_team())