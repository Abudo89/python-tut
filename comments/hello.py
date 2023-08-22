#Comments in Python start with the hash character, #, 
#and extend to the end of the physical line. A comment may appear at the start of a line or 
#following whitespace or code, but not within a string literal. A hash character within a string 
#literal is just a hash character. Since comments are to clarify code and are not interpreted by Python, 
#they may be omitted when typing in examples.

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

#Or, not quite as intended, you can use a multiline string.

#Since Python will ignore string literals that are not assigned to a variable, 
# you can add a multiline string (triple quotes) in your code, and place your comment inside it:

"""
This is a comment
written in
more than just one line
"""
print("Hello, World!")

