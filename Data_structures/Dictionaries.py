# values can change but the keys can not be changed

student_grades = {
    "Alice": 95,
    "Bob": 88,
    "Charlie": 92.5,
    "David": "Incomplete"
}

student_fullname = {"firstname": "Jesse",
                    "secondname": "Appiah",
                    "thirdname": "Andoh"
                    }

# METHODS ON DICTIONARIES

(student_grades.keys())  # gives all keys
(student_grades.get("Alice"))  # gives value of Alice
(student_grades.values())  # gives all values
(student_grades.items())  # gives all items


student_grades.update(student_fullname)  # This adds or merge two tables
(student_grades)


(student_grades["Alice"])
student_grades["Alice"] = 100
(student_grades["Alice"])

# print(student_grades)


# another form of creating dictionary
a = dict()
a["as"] = "asalph"
a["wa"] = "asweda"

print("as" in a)  # checks if a key is is in a dict and return a boolean
if "as" in a:
    print(a["as"])


print(set(a))  # changing a dic to a sets only gives you the keys


# reverse value in dict
def funct(d, v):
    for key in d:
        if d[key] == v:
            return key
    return dict()


print(funct(student_grades, 88))


## EXERCISE###
fav_book = {
    "Title": "Rich Dad Poor Dad",
    "Author": "Robert",
    "Genre": "Self Help"
}


print(fav_book.get("Genre"))
