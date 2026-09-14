"""
Developer domain model.

Demonstrates inheritance from the Employee class.
"""

from employee import Employee


class Developer(Employee):
    """
    Represent a software developer.

    Developer inherits common employee behavior
    from Employee.
    """

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        programming_language: str,
    ) -> None:
        """
        Initialize a developer.

        Args:
            employee_id: Unique employee identifier.
            name: Developer's name.
            salary: Annual salary.
            programming_language: Primary programming language.
        """

        super().__init__(
            employee_id=employee_id,
            name=name,
            salary=salary,
        )

        programming_language = programming_language.strip()

        if not programming_language:
            raise ValueError(
                "Programming language cannot be empty."
            )

        self.programming_language = programming_language

    def write_code(self) -> str:
        """Describe the developer's coding activity."""

        return (
            f"{self.name} is writing "
            f"{self.programming_language} code."
        )

    def work(self) -> str:
        """Describe the developer's work."""

        return (
            f"{self.name} is developing software "
            f"using {self.programming_language}."
        )