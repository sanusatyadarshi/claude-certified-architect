def calculate_average(numbers):
    """Return the arithmetic mean of ``numbers``.

    An empty input has no meaningful mean; 0.0 is returned rather than
    raising ZeroDivisionError.
    """
    if not numbers:
        return 0.0
    total = 0
    for num in numbers:
        total += num
    return total / len(numbers)


def get_user_name(user):
    """Return the user's name, uppercased.

    Returns an empty string when ``user`` is None, is missing a "name"
    key, or has a null name.
    """
    if not user:
        return ""
    name = user.get("name")
    if name is None:
        return ""
    return str(name).upper()