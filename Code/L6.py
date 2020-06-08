# Reading Text File
# @ Michael

# Text read will only read one time
school = open('File/school.txt', 'r')
school_str = school.read()
len(school_str)

# The following code will not work
# school = open('File/school.txt', 'r')
# school.read()
# school_str = school.read()
# len(school_str)

# readlines
# Returns a list of strings, each representing a single line of the file
school = open('File/school.txt', 'r')
school.readlines()
