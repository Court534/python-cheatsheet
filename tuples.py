# Tuples are immutable lists, they cannot be changed

t = (1, 2, 3) # This is a tuple
mylist = [1, 2, 3] # This is a list

print(type(t)) # prints <class 'tuple'>
print(type(mylist)) # prints <class 'list'>

t = ('one', 2)
print(t[0]) # prints 'one'
print(t[-1]) # prints 2

t = ('a', 'a', 'b')
print(t.count('a')) # counts the number of times 'a' appears in the tuple
print(t.index('a')) # prints 0, the index of the first 'a' in the tuple

mylist[0] = 'NEW'
print(mylist) # prints ['NEW', 2, 3]

# t[0] = 'NEW' # This will throw an error because tuples are immutable

# Tuple unpacking is a way to assign multiple variables at once
stock_prices = [('APPL', 200), ('GOOG', 400), ('MSFT', 100)]

for item in stock_prices:
    print(item) # prints ('APPL', 200), ('GOOG', 400), ('MSFT', 100)
    
for ticker, price in stock_prices:
    print(ticker) # prints APPL, GOOG, MSFT
    
for ticker, price in stock_prices:
    print(price + 0.1 * price) # prints 220.0, 440.0, 110.0 (10% increase)
    
# Tuple unpacking to see what employee worked the most hours
work_hours = [('Abby', 100), ('Billy', 400), ('Cassie', 800)]

def employee_check(work_hours):
    current_max = 0
    employee_of_the_month = ''
    
    for employee, hours in work_hours:
        if hours > current_max:
            current_max = hours
            employee_of_the_month = employee
        else:
            pass
    return (employee_of_the_month, current_max)

print(employee_check(work_hours)) # prints ('Cassie', 800)
    