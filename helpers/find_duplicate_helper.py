def sanitize_list_to_single_value(list):
    if (len(list) == 1):
        return list[0]

    if (len(list) == 0):
        return False

    return list
