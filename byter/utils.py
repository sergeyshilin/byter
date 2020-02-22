"""Byter utilities."""

from .constants import TYPES_TABLE


def get_type(c_type):
    """
    Get a format character from the C-language type string.

    For more info refer to
    https://docs.python.org/2/library/struct.html#format-characters

    Examples
    --------
        get_type("unsigned_int") returns "I"
        get_type("long") returns "l"

    Parameters
    ----------
    c_type : str
        C-language type string (e.g. "unsigned_int")

    Returns
    -------
    str
        A format character for `struct` library
    """
    return TYPES_TABLE[c_type]
