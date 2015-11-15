"""
    This is function to print list with intent
"""


def print_books(books_list, intent=False, level=0):
    for sub_list in books_list:
        if isinstance(sub_list, list):
            print_books(sub_list, intent, level + 1)
        else:
            if intent:
                for num in range(level):
                    print("\t"),
            print(sub_list)


books = ['Agile', 1973, ['xp', 1995, ['effective java', 1999]]]
print_books(books, True, 0)
