# Create a collection of these authors and
# the year they kicked the bucket;
# print the collection in the following format:

# Charles Dickens died in 1870.

# Charles Dickens, 1870
# William Thackeray, 1863
# Anthony Trollope, 1882
# Gerard Manley Hopkins, 1889

authors = { # changed variable name to authors
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

# Moved curly bracket from below the for loop to the correct end of the dictionary

for author, date in authors.items(): # comma after 'author' to refer to '[key], [value]', refer to authors regular brackets to call items
    print("%s" % author + " died in " + "%s." % date) # Added brackets, changed variables to match previous code