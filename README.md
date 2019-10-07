# Byter
Python reader/writer for binary objects

## Installation

```
pip install -U byter
```

## Usage Example

```python
with open("/path/to/binary/file", "rb") as data:
    has_data = read_bool(data)
    year = read_short(data)
    month = read_short(data)
    width = read_float(data)
    height = read_float(data)
    text = read_string(data, 70)
    array = read_array(data, 3, 'unsigned_short')

print("has_data:", has_data)
print("year:", year)
print("month:", month)
print("width:", width)
print("height:", height)
print("text:": text)
print("array:", array)

>> has_data: True
   year: 2019
   month: 9
   width: 1280.0
   height: 1024.0
   text: "Hello World!"
   array: [13, 4, 16]
```

## Types allowed to read/write

| C Type | Python type | Size in bytes |
| --- | --- | --- |
| char | string of length 1 | 1 |
| signed char | integer | 1 |
| unsigned char | integer | 1 |
| bool | boolean | 1 |
| short | integer | 2 |
| unsigned short | integer | 2 |
| int | integer | 4 |
| unsigned int | integer | 4 |
| long | integer | 4 |
| unsigned long | integer | 4 |
| long long | integer | 8 |
| unsigned long long | integer | 8 |
| float | float | 4 |
| double | float | 8 |
| char[] | string | |

## Methodes allowed

For each C type from the table in the previous section, there is a `read_` and a `write_` function that performs a reading/writing of a specified number of bytes from the binary object. For example,

```python
a = read_unsigned_long(data)
```

will read 4 consequent bytes from the binary source `data`.

However, to read an array of chars (string) the method is

```python
s = read_string(data, s_len)
```

It is also possible to read an array of bytes using the following method:

```python
arr = read_array(data, size, 'unsigned_short')
```

This will read a sequence of length `size` of unsigned ints, `size  * 2` bytes in total (`short` type is of 2 bytes).
