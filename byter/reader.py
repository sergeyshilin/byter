__all__ = [
    'read_char',
    'read_signed_char',
    'read_unsigned_char',
    'read_bool',
    'read_short',
    'read_unsigned_short',
    'read_int',
    'read_unsigned_int',
    'read_long',
    'read_unsigned_long',
    'read_long_long',
    'read_unsigned_long_long',
    'read_float',
    'read_double',
    'read_string',
    'read_array']

import struct


def read_char(data):
    """Read 1 byte of data as `char`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        str -- Python string of length 1
    """
    return struct.unpack("c", data.read(1))[0]


def read_signed_char(data):
    """Read 1 byte of data as `signed char`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer
    """
    return struct.unpack("b", data.read(1))[0]


def read_unsigned_char(data):
    """Read 1 byte of data as `unsigned char`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer
    """
    return struct.unpack("B", data.read(1))[0]


def read_bool(data):
    """Read 1 byte of data as `bool` type

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        bool -- True or False
    """
    return struct.unpack("?", data.read(1))[0]


def read_short(data):
    """Read 2 bytes of data as `short`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer
    """
    return struct.unpack("h", data.read(2))[0]


def read_unsigned_short(data):
    """Read 2 bytes of data as `unsigned short`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer
    """
    return struct.unpack("H", data.read(2))[0]


def read_int(data):
    """Read 4 bytes of data as `int`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer (int32)
    """
    return struct.unpack("i", data.read(4))[0]


def read_unsigned_int(data):
    """Read 4 bytes of data as `unsigned int`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer (int32)
    """
    return struct.unpack("I", data.read(4))[0]


def read_long(data):
    """Read 4 bytes of data as `long`.
       It is highly recommended to use `read_int(data)` instead.

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer (int32)
    """
    return struct.unpack("l", data.read(4))[0]


def read_unsigned_long(data):
    """Read 4 bytes of data as `unsigned long`
       It is highly recommended to use `read_unsigned_int(data)` instead.

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- Python integer (int32)
    """
    return struct.unpack("L", data.read(4))[0]


def read_long_long(data):
    """Read 8 bytes of data as `long long`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- 8-bytes python integer (int64)
    """
    return struct.unpack("q", data.read(8))[0]


def read_unsigned_long_long(data):
    """Read 8 bytes of data as `unsigned long long`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        int -- 8-bytes python integer (int64)
    """
    return struct.unpack("Q", data.read(8))[0]


def read_float(data):
    """Read 4 bytes of data as `float`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        float -- 4-bytes python float (float32)
    """
    return struct.unpack("f", data.read(4))[0]


def read_double(data):
    """Read 8 bytes of data as `double`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode

    Returns:
        float -- 8-bytes python float (float64)
    """
    return struct.unpack("d", data.read(8))[0]


def read_string(data, s_len):
    """Read `s_len` bytes as `char[]`

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode
        s_len {int} -- Size of the string to read (# of bytes)

    Returns:
        str -- Python string of length `s_len`
    """
    return struct.unpack("%ds" % s_len, data.read(s_len))[0].decode("utf-8")


def read_array(data, size, read_type):
    """Read `size` consequent bytes using `read_type` as a Python list.

    Arguments:
        data {io.BufferedReader} -- File open to read in binary mode
        size {int} -- Number of elements to read
        read_type {function} -- Callback function to read each element of array

    Returns:
        list -- Python list of elemements
    """
    return [read_type(data) for _ in range(size)]
