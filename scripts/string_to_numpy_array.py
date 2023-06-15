def string_to_numpy_array(string: str):
    """Converts a string to a numpy array. Useful for when numpy outputs arrays to the terminal during
    testing that you want to then input again into a script. Only handles 2d arrays.

    Example:
    input:
    "
    [[1 2 3e-1]
    [4 5 6][7 8e-2 9]]
    "
    output:
    numpy array object that is equal to the output of this:
    np.array([1, 2, 3e-1], [4, 5, 6], [7, 8e-2, 9]])

    
    Parameters
    ----------
    string: str
        string of a 2d numpy array that is to be converted into a numpy array.
        
    Returns
    -------
    np.ndarray
        the string turned into a numpy array
    """
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