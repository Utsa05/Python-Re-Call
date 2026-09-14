"""
Manager domain model.

Demonstrates another child class inheriting
from Employee.
"""

from employee import Employee


class Manager(Employee):
    """
    Represent a company manager.

    Manager inherits common employee behavior
    from Employee.
    """

    def __init__(
        self,
        employee_id: str,
        name: str,
        salary: float,
        team_size: int,
    ) -> None:
        """
        Initialize a manager.

        Args:
            employee_id: Unique employee identifier.
            name: Manager's name.
            salary: Annual salary.
            team_size: Number of employees managed.
        """

        super().__init__(
            employee_id=employee_id,
            name=name,
            salary=salary,
        )

        if team_size < 0:
            raise ValueError(
                "Team size cannot be negative."
            )

        self.team_size = team_size

    def calculate_annual_bonus(self) -> float:
        """
        Calculate the manager's annual bonus.

        Managers receive a higher bonus rate.

        Returns:
            Annual bonus amount.
        """

        return self.salary * 0.10

    def manage_team(self) -> str:
        """Describe the manager's team responsibility."""

        return (
            f"{self.name} manages "
            f"a team of {self.team_size} employees."
        )

    def work(self) -> str:
        """Describe the manager's work."""

        return (
            f"{self.name} is managing the team "
            f"and coordinating projects."
        )