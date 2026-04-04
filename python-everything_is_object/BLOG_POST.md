![Mutable, Immutable, Everything Is an Object](blog_header.svg)

# Mutable, Immutable, Everything Is an Object in Python

In Python, variables don't hold values — they reference objects. Every object has an identity (`id()`), a type (`type()`), and rules about whether it can change. Understanding this is key to avoiding subtle bugs.

## id and type

`id()` returns an object's unique identifier; `type()` returns its class. Two names can share the same object or point to different ones with equal values — that's why `==` (value) and `is` (identity) exist.

>>> l1 = [1, 2, 3]
>>> l2 = [1, 2, 3]
>>> l1 == l2  # True — same value
>>> l1 is l2  # False — different objects

## Mutable objects

Lists, dicts, and sets can be changed in place. If two names reference the same list, mutating through one affects the other:

>>> a = [1, 2, 3]
>>> b = a
>>> a.append(4)
>>> b
[1, 2, 3, 4]  # b sees the change — same object

## Immutable objects

Integers, strings, and tuples cannot change in place. "Modifying" them creates a new object and rebinds the name:

>>> a = 1
>>> id_before = id(a)
>>> a += 1
>>> id(a) == id_before  # False — new object

## Why it matters

Mutable objects can be changed through any reference, causing aliasing bugs. Immutable objects are safe from this. To safely copy a list, use slicing:

>>> new = my_list[:]
>>> new == my_list  # True
>>> new is my_list  # False — independent copy

## Function arguments

Python passes arguments by object reference. Mutating a mutable argument affects the caller; rebinding the parameter does not:

>>> def add(items):
...     items.append(4)
>>> l = [1, 2, 3]
>>> add(l)
>>> l
[1, 2, 3, 4]  # mutated

>>> def assign(n, v):
...     n = v  # only rebinds locally
>>> assign(l, [7, 8])
>>> l
[1, 2, 3, 4]  # unchanged

## Advanced takeaways

CPython interns small integers and some strings, so `is` may seem to work for value comparisons in small tests — but don't rely on it. Use `==` for values, `is` only for identity checks like `x is None`. Also note: `a += [4]` mutates a list in place, while `a = a + [4]` creates a new one.

## Publishing URLs
LinkedIn article/post URL: pending manual publication
