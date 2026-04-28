def is_match(pattern, s):
    i = 0  # индекс строки
    j = 0  # индекс шаблона
    star_idx = -1
    match = 0

    while i < len(s):
        # Совпадение или '?'
        if j < len(pattern) and (pattern[j] == s[i] or pattern[j] == '?'):
            i += 1
            j += 1

        # Встретили '*'
        elif j < len(pattern) and pattern[j] == '*':
            star_idx = j
            match = i
            j += 1

        # Несовпадение, но была '*'
        elif star_idx != -1:
            j = star_idx + 1
            match += 1
            i = match

        # Несовпадение и нет '*'
        else:
            return "NO"

    # Проверяем остаток шаблона — там должны быть только '*'
    while j < len(pattern) and pattern[j] == '*':
        j += 1

    return "YES" if j == len(pattern) else "NO"


pattern = "k?t*n"
str = "kitten"

print(is_match(pattern, str))