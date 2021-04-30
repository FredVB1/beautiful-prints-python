
def printNestedData(nestedData: any, maxItemsPerLine: int = 5, indent: int = 4) -> str:

    return _printNestedData(nestedData, indent, maxItemsPerLine)


def _printNestedData(nestedData: any, indent: int,  maxItemsPerLine: int = 5, depth: int = 0) -> str:
    nestedDataTypes = {
        tuple: ("(", ")"),
        dict: ("{", "}"),
        list: ("[", "]"),
        set: ("set(", ")"),
        frozenset: ("frozenset(", ")"),
    }

    spacing = " " * indent
    output = ""

    for index, data in enumerate(nestedData):
        done = False
        if type(nestedData) == dict:
            if type(nestedData[data]) in nestedDataTypes or (type(nestedData[data]) in nestedDataTypes and len(nestedData[data]) > maxItemsPerLine):
                for subData in nestedData[data]:
                    if done is False:
                        if type(subData) in nestedDataTypes or (type(nestedData[data]) in nestedDataTypes and len(nestedData[data]) > maxItemsPerLine):
                            output += _printNestedData(data, indent, maxItemsPerLine, depth=depth + 1)
                            done = True
                            break
            if done is False:
                if index == 0:
                    output += f"\n{spacing * depth}{nestedDataTypes[type(nestedData)][0]}"
                else:
                    output += ","

                output += f"""\n{spacing * (depth + 1)}""" \
                          f""" {f'"{data}"' if type(data) == str else data}:""" \
                          f""" {f'"{nestedData[data]}"' if type(nestedData[data]) == str else nestedData[data]}"""

        else:
            if type(data) in nestedDataTypes or (type(data) in nestedDataTypes and len(data) > maxItemsPerLine):
                done = False
                for subData in data:
                    if done is False:
                        if type(subData) in nestedDataTypes or (type(data) in nestedDataTypes and len(data) > maxItemsPerLine):
                            output += ","
                            output += _printNestedData(data, indent, maxItemsPerLine, depth=depth + 1)
                            done = True
                            break

            if done is False:
                if index == 0:
                    output += f"\n{spacing * depth}" \
                              f"{nestedDataTypes[type(nestedData)][0]}"
                else:
                    output += ","

                output += f"""\n{spacing * (depth + 1)}""" \
                          f"""{f'"{data}"' if type(data) == str else data}"""

    output += f"\n{spacing * depth}" \
              f"{nestedDataTypes[type(nestedData)][1]}"

    return output
