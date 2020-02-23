"""Test all base functions of the package (excluding array read/write)."""

import os
import random
import string

from byter import *

TEST_FILE = "./tests/testfile.byter"
NUMBER_ENTRIES = 10000


def __delete_testfile():
    """
    Delete the file at path `TEST_FILE`.

    This function is called at the beginning of each test.
    """
    if os.path.exists(TEST_FILE):
        os.remove(TEST_FILE)


def test_char():
    """Test [write|read]_char function."""
    __delete_testfile()

    write_values = [
        random.choice(string.ascii_letters).encode("utf-8")
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_char(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_char(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_signed_char():
    """Test [write|read]_signed_char function."""
    __delete_testfile()

    write_values = [
        random.choice(range(-128, 128)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_signed_char(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_signed_char(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_unsigned_char():
    """Test [write|read]_unsigned_char function."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 256)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_unsigned_char(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_unsigned_char(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_bool():
    """Test [write|read]_bool function."""
    __delete_testfile()

    write_values = [
        random.choice([True, False]) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_bool(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_bool(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_short():
    """Test [write|read]_short function."""
    __delete_testfile()

    write_values = [
        random.choice(range(-32768, 32768)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_short(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_short(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_unsigned_short():
    """Test [write|read]_unsigned_short function."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 65536)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_unsigned_short(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_unsigned_short(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_int():
    """Test [write|read]_int function."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**31), 2**31))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_int(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_int(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_unsigned_int():
    """Test [write|read]_unsigned_int function."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**32)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_unsigned_int(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_unsigned_int(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_long():
    """Test [write|read]_long function."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**31), 2**31))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_long(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_long(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_unsigned_long():
    """Test [write|read]_unsigned_long function."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**32)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_unsigned_long(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_unsigned_long(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_long_long():
    """Test [write|read]_long_long function."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**62) + 1, 2**62 - 1))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_long_long(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_long_long(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_unsigned_long_long():
    """Test [write|read]_unsigned_long_long function."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**63 - 1)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_unsigned_long_long(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_unsigned_long_long(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_float():
    """Test [write|read]_float function."""
    __delete_testfile()

    write_values = [
        round(random.uniform(-1 * (2**7), 2**7), 5)
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_float(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = round(read_float(test_file), 5)
            read_values.append(value)

    assert write_values == read_values


def test_double():
    """Test [write|read]_double function."""
    __delete_testfile()

    write_values = [
        round(random.uniform(-1 * (2**63), 2**63), 15)
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_double(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for _ in range(NUMBER_ENTRIES):
            value = read_double(test_file)
            read_values.append(value)

    assert write_values == read_values


def test_string():
    """Test [write|read]_string function."""
    __delete_testfile()

    str_length_min = 10
    str_length_max = 50
    char_dict = string.ascii_lowercase + string.ascii_uppercase + string.digits
    char_dict += " "  # add a whitespace, so it looks more like real words

    write_values = []

    for entry in range(NUMBER_ENTRIES):
        str_length = random.choice(range(str_length_min, str_length_max))
        write_values.append("".join(
            random.choice(char_dict) for _ in range(str_length)))

    value_lengths = [len(v) for v in write_values]

    with open(TEST_FILE, "ab") as test_file:
        for value in write_values:
            write_string(test_file, value)

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        for s_len in value_lengths:
            value = read_string(test_file, s_len)
            read_values.append(value)

    assert write_values == read_values
