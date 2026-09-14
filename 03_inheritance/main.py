"""
Application entry point.
"""

from employe_controller import EmployeeController
from developer import Developer
from manager import Manager


def main() -> None:
    """Start the employee management application."""

    controller = EmployeeController()

    try:
        # --------------------------------------------------
        # Create employees
        # --------------------------------------------------

        developer = Developer(
            employee_id="EMP-001",
            name="Alex",
            salary=85000,
            programming_language="Python",
        )

        manager = Manager(
            employee_id="EMP-002",
            name="Sarah",
            salary=110000,
            team_size=8,
        )

        # --------------------------------------------------
        # Add employees
        # --------------------------------------------------

        controller.add_employee(developer)
        controller.add_employee(manager)

        # --------------------------------------------------
        # Display employees
        # --------------------------------------------------

        print("=" * 60)
        print("EMPLOYEES")
        print("=" * 60)

        controller.show_employees()

        # --------------------------------------------------
        # Developer details
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("DEVELOPER")
        print("=" * 60)

        controller.show_employee_details(developer)

        # --------------------------------------------------
        # Manager details
        # --------------------------------------------------

        print("\n" + "=" * 60)
        print("MANAGER")
        print("=" * 60)

        controller.show_employee_details(manager)

    except ValueError as error:
        print("\nERROR:")
        print(f"Invalid employee data: {error}")

    except TypeError as error:
        print("\nERROR:")
        print(f"Invalid employee type: {error}")

    except Exception as error:
        print("\nERROR:")
        print(f"Unexpected error: {error}")


if __name__ == "__main__":
    main()