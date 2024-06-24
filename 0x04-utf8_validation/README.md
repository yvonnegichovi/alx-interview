# 0x04. UTF-8 Validation

## Algorithm
This project focuses on validating whether a given dataset represents a valid UTF-8 encoding using Python. The key aspects include understanding bitwise operations, the UTF-8 encoding scheme, and Python programming skills.

### Concepts Needed:
- **Bitwise Operations in Python**:
  - Understanding how to manipulate bits in Python, including operations like AND (&), OR (|), XOR (^), NOT (~), shifts (<<, >>).
  - Resources:
    - [Python Bitwise Operators](https://realpython.com/python-bitwise-operators/)

- **UTF-8 Encoding Scheme**:
  - Familiarity with the UTF-8 encoding rules, including how characters are encoded into one or more bytes.
  - Understanding the patterns that represent a valid UTF-8 encoded character.
  - Resources:
    - [UTF-8 Wikipedia](https://en.wikipedia.org/wiki/UTF-8)
    - [Characters, Symbols, and the Unicode Miracle](https://manishearth.github.io/blog/2017/01/14/characters-symbols-and-the-unicode-miracle/)
    - [The Absolute Minimum Every Software Developer Absolutely, Positively Must Know About Unicode and Character Sets](https://www.joelonsoftware.com/2003/10/08/the-absolute-minimum-every-software-developer-absolutely-positively-must-know-about-unicode-and-character-sets-no-excuses/)

- **Data Representation**:
  - How to represent and work with data at the byte level.
  - Handling the least significant bits (LSB) of integers to simulate byte data.

- **List Manipulation in Python**:
  - Iterating through lists, accessing list elements, and understanding list comprehensions.
  - Resources:
    - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

- **Boolean Logic**:
  - Applying logical operations to make decisions within the program.

By studying these concepts and utilizing the resources provided, you will be equipped to tackle the UTF-8 validation project, effectively applying bitwise operations and logical reasoning to determine the validity of UTF-8 encoded data.

### Additional Resource:
- [Mock Technical Interview](https://www.pramp.com/)

## Requirements
### General
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.x)
- All your files must be executable

## Tasks
### 0. UTF-8 Validation
#### Mandatory
Write a method that determines if a given data set represents a valid UTF-8 encoding.

- **Prototype**: `def validUTF8(data):`
- **Return**: `True` if data is a valid UTF-8 encoding, else return `False`
- A character in UTF-8 can be 1 to 4 bytes long
- The data set can contain multiple characters
- The data will be represented by a list of integers
- Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer

Example usage:
```python
#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33]
print(validUTF8(data))

data = [229, 65, 127, 256]
print(validUTF8(data))
```

Expected output:
```bash
carrie@ubuntu:~/0x04-utf8_validation$ ./0-main.py
True
True
False
carrie@ubuntu:~/0x04-utf8_validation$
```

### Repository Structure
```
alx-interview
│
├── 0x04-utf8_validation
│   ├── README.md
│   ├── 0-validate_utf8.py
│   └── 0-main.py
```