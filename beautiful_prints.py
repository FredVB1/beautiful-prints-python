

def beautifulPrint(nestedData: any, maxItemsPerLine: int = 5, indent: int = 4):
    """
    Outputs your passed [nestedData] in a beautiful way.

        The Concept ist that if an item of the nested data is a nested data type or the length of the nested data is
        bigger than the maximum items per line [maxItemsPerLine], it will be put in the next line.

        The information that an item of the nested data is a nested data type, is more important than the maximum items
        per line [maxItemsPerLine]. Therefore [maxItemsPerLine] does not specify the minimum of items per line.

    Currently supported nested data types:
        tuple,
        dict,
        list,
        set,
        frozenset

    No error will be raised if your nested data is not contained in the currently supported data types.


    Args:
        nestedData (any): The nested data you want to print out in a beautiful way.
        maxItemsPerLine (int, optional): Maximum items allowed per line (default = 5).
        indent (int): Indentation with which the data should be formatted.
    """
    from sys import stdout

    stdout.write(_generateBeautifulString(nestedData, indent, maxItemsPerLine))


def generateBeautifulString(nestedData: any, maxItemsPerLine: int = 5, indent: int = 4) -> str:
    """
    Generates a beautifully formatted string containing the passed [nestedData], so you can print nested data in a
    beautiful way to the console.

        The Concept ist that if an item of the nested data is a nested data type or the length of the nested data is
        bigger than the maximum items per line [maxItemsPerLine], it will be put in the next line.

        The information that an item of the nested data is a nested data type, is more important than the maximum items
        per line [maxItemsPerLine]. Therefore [maxItemsPerLine] does not specify the minimum of items per line.

    Currently supported nested data types:
        tuple,
        dict,
        list,
        set,
        frozenset

    No error will be raised if your nested data is not contained in the currently supported data types.


    Args:
        nestedData (any): The nested data you want to print out in a beautiful way.
        maxItemsPerLine (int, optional): Maximum items allowed per line (default = 5).
        indent (int): Indentation with which the data should be formatted.
    """

    return _generateBeautifulString(nestedData, indent, maxItemsPerLine)


def _generateBeautifulString(
        nestedData: any, indent: int, maxItemsPerLine: int = 5, depth: int = 0, isDict: bool = False) -> str:
    nestedDataTypes = {
        tuple: ("(", ")"),
        dict: ("{", "}"),
        list: ("[", "]"),
        set: ("set(", ")"),
        frozenset: ("frozenset(", ")"),
    }

    spacing = " " * indent
    output = ""

    def items(data: any, isDict: bool = False):
        if type(data) in nestedDataTypes:
            if hasattr(data, '__iter__'):
                for subData in data:
                    if type(subData) in nestedDataTypes or \
                            (type(data) in nestedDataTypes and len(data) > maxItemsPerLine):
                        return _generateBeautifulString(
                            data,
                            indent,
                            maxItemsPerLine,
                            depth=depth + 1,
                            isDict=isDict
                        ), True

        return "", False

    for index, data in enumerate(nestedData):
        done = False
        if type(nestedData) == dict:
            if index == 0:
                output += (f"\n{spacing * depth}" if not isDict else " ") + \
                          f"{nestedDataTypes[type(nestedData)][0]}"
            else:
                output += ","

            output += f"""\n{spacing * (depth + 1)}""" \
                      f"""{f'"{data}"' if type(data) == str else data}:"""

            subOutput, done = items(nestedData[data])
            output += subOutput

            if done is False:
                output += f""" {f'"{nestedData[data]}"' if type(nestedData[data]) == str else nestedData[data]}"""

        else:
            if index == 0:
                output += (f"\n{spacing * depth}" if not isDict else " ") + \
                          f"{nestedDataTypes[type(nestedData)][0]}"
            else:
                output += ","

            subOutput, done = items(data)
            output += subOutput

            if done is False:
                output += f"""\n{spacing * (depth + 1)}""" \
                          f"""{f'"{data}"' if type(data) == str else data}"""

    output += f"\n{spacing * depth}" \
              f"{nestedDataTypes[type(nestedData)][1]}"

    return output
