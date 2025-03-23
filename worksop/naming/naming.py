"""Example module demonstrating Python naming conventions and best practices.

This module serves as a practical guide for Python naming conventions following PEP 8.
It includes examples of good and bad naming practices to be used in workshops.
"""

from dataclasses import dataclass
from typing import Any, List, Optional

# Constants should use UPPER_CASE
MAX_CONNECTIONS = 100
DEFAULT_TIMEOUT_MS = 1000


# Class names should use CapWords convention
class CustomerAccount:
    """Example of class naming and proper documentation."""

    def __init__(self, account_id: str) -> None:
        # Instance variables should use snake_case
        self.account_id = account_id
        self._balance = 0.0  # Protected attributes start with single underscore

    def deposit_money(self, amount: float) -> None:
        """Method names should be verbs in snake_case."""
        self._balance += amount


# Bad naming examples (commented out to pass linting)
# class customer_account:  # Wrong: should be CapWords
#     def Deposit_Money():  # Wrong: should be snake_case
#         myVariable = 100  # Wrong: should be my_variable


@dataclass
class NamingBestPractices:
    """Collection of naming best practices with examples."""

    # Good variable names: descriptive and clear
    user_count: int
    first_name: str
    is_active: bool

    # Function parameters should be clear and meaningful
    def calculate_average(self, numbers: List[float]) -> float:
        """Good: clear verb phrase, obvious purpose."""
        return sum(numbers) / len(numbers)

    def get_user_by_id(self, user_id: str) -> Optional[dict[Any, Any]]:
        """Good: describes what it does and what it returns."""
        pass

    # Bad examples (commented out)
    # def calc(self, x):  # Wrong: too vague
    # def get_data(self):  # Wrong: not specific enough
    # tmp = 0  # Wrong: not descriptive
    # def process_stuff(self):  # Wrong: too vague
