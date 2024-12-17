# SPDX-FileCopyrightText: OpenSSF project contributors
# SPDX-License-Identifier: MIT
""" Compliant Code Example """
numbers = ["one", "two", "three"]

print(f"len({numbers}) == {len(numbers)}")


def custom_len(x):
    """ implementing a dodgy version of a build in method """
    return sum(1 for _ in x) + 1


print(f"len({numbers}) == {len(numbers)}")
