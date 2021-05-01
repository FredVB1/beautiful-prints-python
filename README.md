# print-nested-data-python
Beautiful prints for nested data (iterables) in python.

## How to use it?
### Installation
Install it using ```pip install beautiful-prints```

### Usage
You can either use [`printNestedData`](https://github.com/FredVB1/print-nested-data-python/blob/575e64bfd299774f87b05fb0eb7bb8342d04a326/printNestedData.py#L3)
to directly write the formatted string to the current system output (console) or 
[`generateBeautifulString`](https://github.com/FredVB1/print-nested-data-python/blob/575e64bfd299774f87b05fb0eb7bb8342d04a326/printNestedData.py#L33)
to get the formatted string and mess around with it:
```
beautifullyFormatedString = generateBeautifulString(yourNestedData)
```
Output it directly:
```
printNestedData(yourNestedData)
```
Both functions have the optional parameters `maxItemsPerLine` and `indent`. The former to set the maximum items per 
line (default = 5) and the latter to set the indent (default = 4). 

## What's the concept?
The concept is to print nested data in a json like format, but different ;D

### A quick example:
```
nestedData = {"key1": [1, 2, 3, 4], "key2": [1, 2, 3, 4]}
```
beautiful output using [`printNestedData`](https://github.com/FredVB1/print-nested-data-python/blob/575e64bfd299774f87b05fb0eb7bb8342d04a326/printNestedData.py#L3):
```
{
    "key1": [1, 2, 3, 4], 
    "key2": [1, 2, 3, 4]
}
```
Now this isn't quite json like, right? Json formatted using [`json.dumps`](https://docs.python.org/3/library/json.html), 
it would look like this:
```
{
    "key1": [
        1, 
        2, 
        3, 
        4
    ], 
    "key2": [
        1, 
        2, 
        3, 
        4
    ]
}
```
Yes. This is because the items from the nested data are only printed into the next line if either of their sub data is 
equally a nested data type or the length of it exceeds the maximum items count per line.

### Currently supported nested data types
* lists
* tuples
* dicts
* sets
* frozensets

Note: There won't be raised an error if the used data type is not listed. It'll work, but it will probably be ugly. 
Additionally, any not iterable sub data type such as
[`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64) is supported.

## Examples
An example using a Dict containing strings as keys and lists out of tuples, sets and frozensets as values
```
exampleDict = {
    "key1": [
        [
            ("key_1_list1_tuple1_1", "key_1_list1_tuple1_2"),
            {"key_1_list1_tuple2_1", "key_1_list1_tuple2_2"},  # Here we have a set ;)
            frozenset({"key_1_list1_tuple3_1", "key_1_list1_tuple3_2"}),  # And here a frozenset ;)
            ("key_1_list1_tuple4_1", "key_1_list1_tuple4_2"),
            ("key_1_list1_tuple5_1", "key_1_list1_tuple5_2")
        ],
        [
            ("key_1_list2_tuple1_1", "key_1_list2_tuple1_2"),
            ("key_1_list2_tuple2_1", "key_1_list2_tuple2_2"),
            ("key_1_list2_tuple3_1", "key_1_list2_tuple3_2"),
            ("key_1_list2_tuple4_1", "key_1_list2_tuple4_2"),
            ("key_1_list2_tuple5_1", "key_1_list2_tuple5_2")
        ]
    ],
    "key2": [
        (
            "key_2_list1_tuple1_1",
            "key_2_list1_tuple1_2",
            "key_2_list1_tuple1_3",
            "key_2_list1_tuple1_4",
            "key_2_list1_tuple1_5",
            "key_2_list1_tuple1_6"
        ),
        ("key_2_list1_tuple2_1", "key_2_list1_tuple2_2"),
        ("key_2_list1_tuple3_1", "key_2_list1_tuple3_2"),
        ("key_2_list1_tuple4_1", "key_2_list1_tuple4_2"),
        ("key_2_list1_tuple5_1", "key_2_list1_tuple5_2")
    ]
}
```
Output without formatting:
```
{'key1': [[('key_1_list1_tuple1_1', 'key_1_list1_tuple1_2'), {'key_1_list1_tuple2_2', 'key_1_list1_tuple2_1'}, frozenset({'key_1_list1_tuple3_1', 'key_1_list1_tuple3_2'}), ('key_1_list1_tuple4_1', 'key_1_list1_tuple4_2'), ('key_1_list1_tuple5_1', 'key_1_list1_tuple5_2')], [('key_1_list2_tuple1_1', 'key_1_list2_tuple1_2'), ('key_1_list2_tuple2_1', 'key_1_list2_tuple2_2'), ('key_1_list2_tuple3_1', 'key_1_list2_tuple3_2'), ('key_1_list2_tuple4_1', 'key_1_list2_tuple4_2'), ('key_1_list2_tuple5_1', 'key_1_list2_tuple5_2')]], 'key2': [('key_2_list1_tuple1_1', 'key_2_list1_tuple1_2', 'key_2_list1_tuple1_3', 'key_2_list1_tuple1_4', 'key_2_list1_tuple1_5', 'key_2_list1_tuple1_6'), ('key_2_list1_tuple2_1', 'key_2_list1_tuple2_2'), ('key_2_list1_tuple3_1', 'key_2_list1_tuple3_2'), ('key_2_list1_tuple4_1', 'key_2_list1_tuple4_2'), ('key_2_list1_tuple5_1', 'key_2_list1_tuple5_2')]}
```
Output using [`printNestedData`](https://github.com/FredVB1/print-nested-data-python/blob/575e64bfd299774f87b05fb0eb7bb8342d04a326/printNestedData.py#L3):
```
{
     "key1": [
        [
            ('key_1_list1_tuple1_1', 'key_1_list1_tuple1_2'),
            {'key_1_list1_tuple2_2', 'key_1_list1_tuple2_1'},
            frozenset({'key_1_list1_tuple3_1', 'key_1_list1_tuple3_2'}),
            ('key_1_list1_tuple4_1', 'key_1_list1_tuple4_2'),
            ('key_1_list1_tuple5_1', 'key_1_list1_tuple5_2')
        ],
        [
            ('key_1_list2_tuple1_1', 'key_1_list2_tuple1_2'),
            ('key_1_list2_tuple2_1', 'key_1_list2_tuple2_2'),
            ('key_1_list2_tuple3_1', 'key_1_list2_tuple3_2'),
            ('key_1_list2_tuple4_1', 'key_1_list2_tuple4_2'),
            ('key_1_list2_tuple5_1', 'key_1_list2_tuple5_2')
        ]
    ],
     "key2": [
        (
            "key_2_list1_tuple1_1",
            "key_2_list1_tuple1_2",
            "key_2_list1_tuple1_3",
            "key_2_list1_tuple1_4",
            "key_2_list1_tuple1_5",
            "key_2_list1_tuple1_6"
        ),
        ('key_2_list1_tuple2_1', 'key_2_list1_tuple2_2'),
        ('key_2_list1_tuple3_1', 'key_2_list1_tuple3_2'),
        ('key_2_list1_tuple4_1', 'key_2_list1_tuple4_2'),
        ('key_2_list1_tuple5_1', 'key_2_list1_tuple5_2')
    ]
}
```
Now, what about [`pprint`](https://docs.python.org/3/library/pprint.html)?
Well, see for your self:
```
{'key1': [[('key_1_list1_tuple1_1', 'key_1_list1_tuple1_2'),
           {'key_1_list1_tuple2_2', 'key_1_list1_tuple2_1'},
           frozenset({'key_1_list1_tuple3_1', 'key_1_list1_tuple3_2'}),
           ('key_1_list1_tuple4_1', 'key_1_list1_tuple4_2'),
           ('key_1_list1_tuple5_1', 'key_1_list1_tuple5_2')],
          [('key_1_list2_tuple1_1', 'key_1_list2_tuple1_2'),
           ('key_1_list2_tuple2_1', 'key_1_list2_tuple2_2'),
           ('key_1_list2_tuple3_1', 'key_1_list2_tuple3_2'),
           ('key_1_list2_tuple4_1', 'key_1_list2_tuple4_2'),
           ('key_1_list2_tuple5_1', 'key_1_list2_tuple5_2')]],
 'key2': [('key_2_list1_tuple1_1',
           'key_2_list1_tuple1_2',
           'key_2_list1_tuple1_3',
           'key_2_list1_tuple1_4',
           'key_2_list1_tuple1_5',
           'key_2_list1_tuple1_6'),
          ('key_2_list1_tuple2_1', 'key_2_list1_tuple2_2'),
          ('key_2_list1_tuple3_1', 'key_2_list1_tuple3_2'),
          ('key_2_list1_tuple4_1', 'key_2_list1_tuple4_2'),
          ('key_2_list1_tuple5_1', 'key_2_list1_tuple5_2')]}
```
Above is the output when using `pprint` from the [`pprint`](https://docs.python.org/3/library/pprint.html) module 
without changing any default values and passing parameters. [`printNestedData`](https://github.com/FredVB1/print-nested-data-python/blob/575e64bfd299774f87b05fb0eb7bb8342d04a326/printNestedData.py#L3)
simply works by default and is easy...

And what about [`json.dumps`](https://docs.python.org/3/library/json.html)?
Well if you don't need tuples or sets or frozensets or any 'special' data type such as 
[`numpy.int64`](https://numpy.org/doc/stable/reference/arrays.scalars.html#numpy.int64) you can use it, though have a 
look under [A quick example](#A quick example:) and decide for yourself what you find more beautiful.
¯\_(ツ)_/¯
```
'json.dumps' won't work with this example :(
```
