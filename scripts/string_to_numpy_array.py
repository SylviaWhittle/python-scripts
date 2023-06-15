def string_to_numpy_array(string: str):
    # Remove new lines
    string = string.replace("\n", "")
    string = string[1:-1]
    array = []
    number_string = ""
    row_floats = []
    while True:
        # Create new row
        string = string[1:]
        if len(string) <= 0:
            break

        char = string[0]
        if char == " ":
            if number_string != "":
                current_float = float(number_string)
                row_floats.append(current_float)
                number_string = ""
        elif char == "]":
            if number_string != "":
                current_float = float(number_string)
                row_floats.append(current_float)
                number_string = ""

            array.append(np.array(row_floats))
            row_floats = []
        elif char == "[":
            pass
        else:
            number_string += char
    return array