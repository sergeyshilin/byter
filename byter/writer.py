"""Byter write functions."""

# yapf: disable
__all__ = [
    "write_char",
    "write_signed_char",
    "write_unsigned_char",
    "write_bool",
    "write_short",
    "write_unsigned_short",
    "write_int",
    "write_unsigned_int",
    "write_long",
    "write_unsigned_long",
    "write_long_long",
    "write_unsigned_long_long",
    "write_float",
    "write_double",
    "write_string",
    "write_array"
]
# yapf: enable

import struct

from .utils import get_type


def write_char(data, value):
    """
    Write 1 byte of data as `char`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : bytes
        Python string of length of 1, encoded as bytes
    """
    s_type = "=%s" % get_type("char")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_signed_char(data, value):
    """
    Write 1 byte of data as `signed char`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("signed_char")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_unsigned_char(data, value):
    """
    Write 1 byte of data as `unsigned char`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("unsigned_char")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_bool(data, value):
    """
    Write 1 byte of data as `bool` type.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : bool
        True or False
    """
    s_type = "=%s" % get_type("bool")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_short(data, value):
    """
    Write 2 bytes of data as `short`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("short")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_unsigned_short(data, value):
    """
    Write 2 bytes of data as `unsigned short`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("unsigned_short")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_int(data, value):
    """
    Write 4 bytes of data as `int`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("int")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_unsigned_int(data, value):
    """
    Write 4 bytes of data as `unsigned int`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("unsigned_int")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_long(data, value):
    """
    Write 4 bytes of data as `long`.

    It is highly recommended to use `write_int(data, value)` instead.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("long")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_unsigned_long(data, value):
    """
    Write 4 bytes of data as `unsigned long`.

    It is highly recommended to use `write_unsigned_int(data, value)` instead.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("unsigned_long")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_long_long(data, value):
    """
    Write 8 bytes of data as `long long`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("long_long")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_unsigned_long_long(data, value):
    """
    Write 8 bytes of data as `unsigned long long`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : int
        Python integer
    """
    s_type = "=%s" % get_type("unsigned_long_long")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_float(data, value):
    """
    Write 4 bytes of data as `float`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : float
        Python float
    """
    s_type = "=%s" % get_type("float")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_double(data, value):
    """
    Write 8 bytes of data as `double`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : float
        Python float
    """
    s_type = "=%s" % get_type("double")
    bytes_data = struct.pack(s_type, value)
    data.write(bytes_data)


def write_string(data, value):
    """
    Write Python string as `char[]`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    value : str
        Python string
    """
    s_type = "=%ds" % len(value)
    bytes_data = struct.pack(s_type, value.encode("utf-8"))
    data.write(bytes_data)


def write_array(data, values, c_type):
    """
    Write a list of elements, each of type `c_type`.

    Parameters
    ----------
    data : io.BufferedWriter
        File open to write in binary mode
    values : list | tuple
        Python iterable object
    c_type : str
        C-language type string (e.g. "unsigned_int")
    """
    s_type = get_type(c_type)
    format_string = "=%d%s" % (len(values), s_type)  # 10i --> write 10 int's
    bytes_data = struct.pack(format_string, *values)
    data.write(bytes_data)
