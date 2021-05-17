import json
from pprint import pprint
from beautiful_prints import beautifulPrint


# Contains a dict, lists, tuples, a set and a frozenset.
dict_lists = {
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

print("\nNested data out of a dict, lists and tuples, a set and a frozenset not formatted: ")
print(dict_lists)

print("\nNested data out of a dict, lists and tuples, a set and a frozenset formatted using 'pprint':")
pprint(dict_lists)

print("\nNested data out of a dict, lists and tuples, a set and a frozenset formatted using 'json.dumps':")
try:
    print(json.dumps(dict_lists, indent=4))
except Exception:
    print("'json.dumps' won't work with this example :(")


print("\nNested data out of a dict, lists, tuples, a set and a frozenset formatted using 'printNestedData':")
beautifulPrint(dict_lists)
