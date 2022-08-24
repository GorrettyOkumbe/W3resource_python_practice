#!/usr/bin/python3
"""module for question 7"""


# Sample String : 'The lyrics is not that poor!'
#                 'The lyrics is poor!'
# Expected Result : 'The lyrics is good!'
#                   'The lyrics is poor!'


def main():
    string = "The lyrics is not"
    org_str = string.split(' ')
    return org_str


def remove_substring():
    a, b = 0, 0
    checker = [
        'poor', 'poor,', 'poor!', 'poor.',
        'not', 'not,', 'not!', 'not.']

    org_str = main()

    for el in org_str:
        if el in checker and el in org_str:
            if 'not' in el:
                a = org_str.index(el)
            elif 'poor' in el:
                b = org_str.index(el) 
    if a < b:
        del org_str[a:b + 1]

    return org_str


def get_index_not():
    x = main()
    new_str = " ".join(x)
    return new_str.find("not")

    # return (x.index('not')


def add_suffix():
    suffix = "good"
    index = get_index_not()

    if index > 0:
        first_part = remove_substring()[:index]
        last_part = remove_substring()[index:]
        first_part.append(suffix)
        first_part.extend(last_part)
        return first_part
    else:
        return main()


print(get_index_not())


if __name__ == "__main__":
    string = ''

    for x in add_suffix():
        string += x + ' '

    print(string)
