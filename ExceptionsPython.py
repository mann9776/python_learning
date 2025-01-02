
ItemsInCart = 0
#  2 items will be added in the cart
if ItemsInCart != 2: #    raise Exception("Number of Products in cart not matched.")  # as condition not matched it raised exception
    pass    # we can nullified if with pass keyword

# For assert keyword, condition is always true in python, if condition doesn't return true, then it breaks the code.

assert(ItemsInCart == 0)

# when we write a code, we know code may fail but we don't want test case to stop when it come across the failure then we can wrap the specific code in try block.
# So that exception raised in try block then test will be sent to another block called catch. So, test will not failed in execution
# Otherwise test will fail if it is not catched.

# try, catch or except

try:
    with open('filename.txt', 'r') as reader:
        reader.read()

except:
    print("Somehow I reached to exception block as try block code failed")

# If wants to print original error message which Python throws not our cutomised message below code helps
try:
    with open('filename.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print("cleaning up resources")
# finally keyword used where you need to clean up the cookies or junk data came due to test failure
# finally keyword will be working with try and except, and it executes always whether test is failing in try block and moving to except or test is passed.

