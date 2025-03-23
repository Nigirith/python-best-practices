"""Example module demonstrating Python type hints best practices.

This module shows how to use type hints effectively and explains their benefits:
- Better code documentation
- Catch errors early through static type checking
- Improved IDE support
- More maintainable code
"""

from dataclasses import dataclass
from typing import Dict, List, Optional, TypedDict, Union

from pydantic import BaseModel, Field, ValidationError


# Basic type hints
def calculate_total(prices: List[float]) -> float:
    """Simple example of function parameter and return type hints."""
    return sum(prices)


# Type hints with classes
@dataclass
class User:
    """Example of type hints in a dataclass."""

    user_id: str
    name: str
    age: int
    email: Optional[str] = None  # Optional field


# Common pitfalls (commented out)
# def wrong_hints(x: str) -> None:
#     return x  # Wrong: returns value despite None return hint
#
# def missing_hints(x):  # Wrong: missing type hints
#     return x + 1


# Union types (Python 3.10+ can use | instead)
def process_id(user_id: Union[int, str]) -> str:
    return str(user_id)


# Type aliases
UserID = str
Timestamp = float


def log_user_action(user_id: UserID, timestamp: Timestamp) -> None:
    """Example of type aliases for better code readability."""
    print(f"User {user_id} acted at {timestamp}")


# TypedDict examples
class UserProfile(TypedDict):
    """TypedDict for representing user profile data structure."""

    name: str
    age: int
    email: str


class UserProfileOptional(TypedDict, total=False):
    """TypedDict with optional fields (total=False)."""

    name: str
    age: int
    email: str  # All fields are optional due to total=False


def process_user_data(profile: UserProfile) -> None:
    """Example of using TypedDict for structured dictionaries."""
    print(f"Processing user {profile['name']}, age {profile['age']}")


# Comparison: TypedDict vs regular dict annotation
def bad_dict_typing(data: Dict[str, str]) -> None:  # Too permissive
    """Anti-pattern: using generic Dict type."""
    print(data["name"])  # No guarantee 'name' exists


def good_dict_typing(data: UserProfile) -> None:  # Strict typing
    """Good practice: using TypedDict."""
    print(data["name"])  # TypedDict ensures 'name' exists


# Pydantic BaseModel examples
class UserModel(BaseModel):
    """Pydantic model for user data with validation."""

    name: str = Field(..., min_length=2)
    age: int = Field(..., ge=0, lt=150)
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")


def demonstrate_pydantic_validation() -> None:
    """Example showing Pydantic validation and error handling."""
    try:
        # Valid data
        user = UserModel(name="John", age=30, email="john@example.com")
        print(f"Valid user: {user.model_dump_json()}")

        # Invalid data (will raise ValidationError)
        invalid_user = UserModel(  # noqa
            name="J",  # too short
            age=200,  # age out of range
            email="invalid-email",  # invalid email format
        )
    except ValidationError as e:
        print(f"Validation error: {e}")


# Comparison: TypedDict vs BaseModel usage
def compare_typing_approaches() -> None:
    """Demonstrate difference between TypedDict and BaseModel."""
    # TypedDict - only static type checking
    user_dict: UserProfile = {  # noqa
        "name": "John",
        "age": 30,
        "email": "john@example.com",
    }  # No runtime validation

    # Pydantic - runtime validation and conversion
    try:
        user_model = UserModel(
            name="John",
            # String will be converted to int
            age="30",  # type: ignore
            email="john@example.com",
        )
        print(f"Parsed age: {user_model.age} (type: {type(user_model.age)})")
    except ValidationError as e:
        print(f"Validation failed: {e}")


# Example usage (commented out)
# valid_profile: UserProfile = {
#     "name": "John",
#     "age": 30,
#     "email": "john@example.com"
# }  # Type checker ensures all required fields
