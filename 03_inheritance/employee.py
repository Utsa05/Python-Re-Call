"""
Base employee domain model.

Demonstrates the parent/base class in inheritance.
"""


class Employee:
    """
    Represent a general employee.

    This is the parent class.
    """

    company_name = "Tech Solutions Ltd"

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
    ) -> None:
        """
        Initialize an employee.

        Args:
            employee_id: Unique employee identifier.
            name: Employee's name.
            salary: Employee's annual salary.

        Raises:
            ValueError: If employee information is invalid.
        """

        employee_id = employee_id.strip()
        name = name.strip()

        if not employee_id:
            raise ValueError(
                "Employee ID cannot be empty."
            )

        if not name:
            raise ValueError(
                "Employee name cannot be empty."
            )

        if salary < 0:
            raise ValueError(
                "Salary cannot be negative."
            )

        self.employee_id = employee_id
        self.name = name
        self.salary = salary

    def get_details(self) -> str:
        """Return common employee information."""

        return (
            f"ID: {self.employee_id}\n"
            f"Name: {self.name}\n"
            f"Salary: ${self.salary:,.2f}"
        )

    def calculate_annual_bonus(self) -> float:
        """
        Calculate the standard employee bonus.

        Returns:
            Annual bonus amount.
        """

        return self.salary * 0.05

    def work(self) -> str:
        """
        Describe general employee work.

        Returns:
            Work description.
        """

        return f"{self.name} is working."

    def __str__(self) -> str:
        """Return a readable employee representation."""

        return (
            f"{self.name} | "
            f"{self.employee_id}"
        )