def calculate_sum(num1, num2):
    result = num1 + num2
   print("The sum is:", result)  # IndentationError
    return reslt  # NameError and potential SyntaxError

my_number = "ten"
total = calculate_sum(5, my_number)  # TypeError
