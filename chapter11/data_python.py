def find_closest(look_for, target_data_list):
    def whats_the_difference(first, second):
        if first < second:
            return second - first
        return first - second

    max_diff = 9999999
    for each in target_data_list:
        diff = whats_the_difference(each, look_for)
        if diff == 0:
            found_it = look_for
            break
        elif diff < max_diff:
            max_diff = diff
            found_it = each
    return found_it


print(find_closest(5, [1, 2, 3, 4, 5.5, 4.5, 6, 8]))
