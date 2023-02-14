# Author: Justin Huang
# GitHub username: huangjus
# Date: 2/14/23
# Description: This function takes a list of first names as input,
#              and returns a new list that contains only those names that start with the letter "K",
#              with the surname "Kardashian" added to each one.

def add_surname(names):
    """Return a list of names that start with 'K' and have 'Kardashian' added as the surname.

    names: A list of first names to filter and modify.
    Returns: a new list containing the filtered names with 'Kardashian' added as the surname.
    """

    return [name + " Kardashian" for name in names if name.startswith("K")]
