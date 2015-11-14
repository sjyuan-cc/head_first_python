movies = ['Think in Java', 1975, 'TDD', 2015, "Agi'le", 1993]
print(movies)
print(movies[2])

print(len(movies))
movies.append('Effect Java')
print(len(movies))

last = movies.pop()
print('pop = ' + last)
print(movies)

movies.extend(['XP', 'Core Java'])
print(movies)

movies.remove('TDD')
print(movies)

movies.insert(3, "CD")
print(movies)

count = movies.count("Agi'le")
print(count)

for movie in movies:
    print(movie)

index = 0
while index < len(movies):
    print(movies[index])
    index += 1

books = ['Agile', 1973, ['xp', 1995, ['effective java', 1999]]]
print(books[2][2][0])
print(books)
for book in books:
    if isinstance(book, list):
        for subBook in book:
            if isinstance(subBook, list):
                for sub2Book in subBook:
                    print(sub2Book)
            else:
                print(subBook)
    else:
        print(book)

"""
    This is function
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


print_books(books, True, 0)

isList = isinstance(books, list)
print(isList)

print dir(__builtins__)
