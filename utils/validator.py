# utils/validator.py

from typing import Optional

VALID_CATEGORIES = ["Food", "Travel", "Bills", "Shopping", "Other"]

def validate_amount(amount_str: str) -> Optional[float]:
    """
    Validates that the amount is a positive number.

    Args:
        amount_str (str): User input for amount

    Returns:
        Optional[float]: Returns float if valid, None if invalid
    """
    try:
        amount = float(amount_str)
        if amount <= 0:
            return None
        return amount
    except ValueError:
        return None


def validate_category(category: str) -> Optional[str]:
    """
    Validates that the category is one of the allowed categories.

    Args:
        category (str): User input for category

    Returns:
        Optional[str]: Returns the properly capitalized category if valid, None if invalid
    """
    category = category.strip().capitalize()
    return category if category in VALID_CATEGORIES else None