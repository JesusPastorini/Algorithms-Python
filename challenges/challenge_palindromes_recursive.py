def is_palindrome_recursive(word, low_index, high_index):
    if len(word) == 0:
        return False

    # Verificar se a palavra é um palíndromo
    def check_palindrome(left, right):
        if left >= right:
            return True
        if word[left] == word[right]:
            return check_palindrome(left + 1, right - 1)
        return False

    return check_palindrome(0, len(word) - 1)
