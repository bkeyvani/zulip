"""
String Utilities:

This module helps in converting strings from one type to another.

Currently we have strings of 3 semantic types:

1.  text strings: These strings are used to represent all textual data,
    like people's names, stream names, content of messages, etc.
    These strings can contain non-ASCII characters, so its type should be
    six.text_type (which is `str` in python 3 and `unicode` in python 2).

2.  binary strings: These strings are used to represent binary data.
    This should be of type six.binary_type (which is `bytes` in python 3
    and `str` in python 2).

3.  native strings: These strings are for internal use only.  Strings of
    this type are not meant to be stored in database, displayed to end
    users, etc.  Things like exception names, parameter names, attribute
    names, etc should be native strings.  These strings should only
    contain ASCII characters and they should have type `str`.

There are 3 utility functions provided for converting strings from one type
to another - force_text, force_bytes, force_str

Interconversion between text strings and binary strings can be done by
using encode and decode appropriately or by using the utility functions
force_text and force_bytes.

It is recommended to use the utility functions for other string conversions.
"""

import six
from six import text_type, binary_type
from typing import Any, Mapping, Union, TypeVar

NonBinaryStr = TypeVar('NonBinaryStr', str, text_type)
# This is used to represent text or native strings

def force_text(s):
    # type: (Union[text_type, binary_type]) -> text_type
    """converts a string to a text string"""
    if isinstance(s, text_type):
        return s
    elif isinstance(s, binary_type):
        return s.decode('utf-8')
    else:
        raise ValueError("force_text expects a string type")

def force_bytes(s):
    # type: (Union[text_type, binary_type]) -> binary_type
    """converts a string to binary string"""
    if isinstance(s, binary_type):
        return s
    elif isinstance(s, text_type):
        return s.encode('utf-8')
    else:
        raise ValueError("force_bytes expects a string type")

def force_str(s):
    # type: (Union[text_type, binary_type]) -> str
    """converts a string to a native string"""
    if isinstance(s, str):
        return s
    elif isinstance(s, text_type):
        return s.encode('utf-8')
    elif isinstance(s, binary_type):
        return s.decode('utf-8')
    else:
        raise ValueError("force_str expects a string type")

def dict_with_str_keys(dct):
    # type: (Mapping[NonBinaryStr, Any]) -> Dict[str, Any]
    """applies force_str on the keys of a dict (non-recursively)"""
    return {force_str(key): value for key, value in six.iteritems(dct)}
