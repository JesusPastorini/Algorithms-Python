def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide o array ao meio
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursivamente aplica o merge_sort a ambas as metades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combina as metades ordenadas
    result = []
    i = j = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            result.append(left_half[i])
            i += 1
        else:
            result.append(right_half[j])
            j += 1

    result.extend(left_half[i:])
    result.extend(right_half[j:])
    
    return result


def is_anagram(first_str, second_str):
    if not first_str and not second_str:
        return ("", "", False)

    str1 = merge_sort(list(first_str.lower().replace(" ", "")))
    str2 = merge_sort(list(second_str.lower().replace(" ", "")))

    result = ("".join(str1), "".join(str2), str1 == str2)
    return result
