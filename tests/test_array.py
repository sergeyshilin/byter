"""Test all possible read_array and write_array cases."""

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


def test_array_char():
    """Test [write|read]_array function with `char` data."""
    __delete_testfile()

    write_values = [
        random.choice(string.ascii_letters).encode("utf-8")
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "char")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "char")

    assert write_values == read_values


def test_array_signed_char():
    """Test [write|read]_array function with `signed_char` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(-128, 128)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "signed_char")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "signed_char")

    assert write_values == read_values


def test_array_unsigned_char():
    """Test [write|read]_array function with `unsigned_char` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 256)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "unsigned_char")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "unsigned_char")

    assert write_values == read_values


def test_array_bool():
    """Test [write|read]_array function with `bool` data."""
    __delete_testfile()

    write_values = [
        random.choice([True, False]) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "bool")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "bool")

    assert write_values == read_values


def test_array_short():
    """Test [write|read]_array function with `short` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(-32768, 32768)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "short")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "short")

    assert write_values == read_values


def test_array_unsigned_short():
    """Test [write|read]_array function with `unsigned_short` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 65536)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "unsigned_short")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "unsigned_short")

    assert write_values == read_values


def test_array_int():
    """Test [write|read]_array function with `int` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**31), 2**31))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "int")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "int")

    assert write_values == read_values


def test_array_unsigned_int():
    """Test [write|read]_array function with `unsigned_int` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**32)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "unsigned_int")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "unsigned_int")

    assert write_values == read_values


def test_array_long():
    """Test [write|read]_array function with `long` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**31), 2**31))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "long")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "long")

    assert write_values == read_values


def test_array_unsigned_long():
    """Test [write|read]_array function with `unsigned_long` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**32)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "unsigned_long")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "unsigned_long")

    assert write_values == read_values


def test_array_long_long():
    """Test [write|read]_array function with `long_long` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(-1 * (2**62) + 1, 2**62 - 1))
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "long_long")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "long_long")

    assert write_values == read_values


def test_array_unsigned_long_long():
    """Test [write|read]_array function with `unsigned_long_long` data."""
    __delete_testfile()

    write_values = [
        random.choice(range(0, 2**63 - 1)) for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "unsigned_long_long")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES,
                                 "unsigned_long_long")

    assert write_values == read_values


def test_array_float():
    """Test [write|read]_array function with `float` data."""
    __delete_testfile()

    write_values = [
        round(random.uniform(-1 * (2**7), 2**7), 5)
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "float")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "float")
        read_values = [round(value, 5) for value in read_values]

    assert write_values == read_values


def test_array_double():
    """Test [write|read]_array function with `double` data."""
    __delete_testfile()

    write_values = [
        round(random.uniform(-1 * (2**63), 2**63), 15)
        for _ in range(NUMBER_ENTRIES)
    ]

    with open(TEST_FILE, "ab") as test_file:
        write_array(test_file, write_values, "double")

    read_values = []

    with open(TEST_FILE, "rb") as test_file:
        read_values = read_array(test_file, NUMBER_ENTRIES, "double")

    assert write_values == read_values
