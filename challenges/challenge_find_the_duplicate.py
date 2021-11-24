from helpers.find_duplicate_helper import sanitize_list_to_single_value


def find_duplicate(nums):
    numbers_set = []
    duplicated_numbers = []
    
    if len(nums) <= 1:
        return False

    for num in nums:
        if isinstance(num, str) or num < 0:
            return False

        if num not in numbers_set:
            numbers_set.append(num)
        elif num not in duplicated_numbers:
            duplicated_numbers.append(num)

    return sanitize_list_to_single_value(duplicated_numbers)
