KAPREKAR_CONSTANT = 6174


def iterate(n, c):
    if (n == KAPREKAR_CONSTANT):
        return c
    if (len(str(n)) == 3):
        n = int(str(n) + '0')
    sep = ''
    asc = int(sep.join(sorted(str(n))))
    desc = int(sep.join(sorted(str(n), reverse=True)))
    s = desc - asc
    return iterate(s, c+1)


def num_kaprekar_iterations(n):
  # Fill this in.
    return iterate(n, 0)


print(num_kaprekar_iterations(123))
# 3
# Explanation:
#  3210 - 123 = 3087
#  8730 - 0378 = 8352
#  8532 - 2358 = 6174 (3 iterations)
