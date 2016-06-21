# there is three students, lloyd, alice and tyler. They have few data show under there name, name, homework, quzzes and tests.
lloyd = {
    "name": "Lloyd",
    "homework": [90,0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# these 3 students is in a list called students.
students = [lloyd, alice, tyler]
# There is a for loop here:
for student in students:
    print "name: %s" % student["name"]
    print "homework: %s" % student["homework"]
    print "quizzes: %s" % student["quizzes"]
    print "tests: %s" % student["tests"]