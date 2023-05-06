def cap_text(text):
    
    ''' Takes a string and will capitalize the first letter of each word '''
    
    return text.capitalize()

print(cap_text("hello there"))

# Test output:
# Hello
# F.
# ======================================================================
# FAIL: test_multiple_worlds (__main__.TestCap)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "test_cap.py", line 14, in test_multiple_worlds
#     self.assertEqual(result, "Hello There!")
# AssertionError: 'Hello there!' != 'Hello There!'
# - Hello there!
# ?       ^
# + Hello There!
# ?       ^


# ----------------------------------------------------------------------
# Ran 2 tests in 0.003s

# FAILED (failures=1)

def cap_text(text):
    
    ''' Takes a string and will capitalize the first letter of each word '''
    
    return text.title()

print(cap_text("hello there"))

# Test output:
# Hello There
# ..
# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# OK
    
    