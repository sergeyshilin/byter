# Byter
Python reader/writer for binary objects

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
arr = read_array(data, size, read_unsigned_int)
```

This will read a sequence of length `size` of unsigned ints, `size  * 4` bytes in total.
