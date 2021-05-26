
def arithmetic_arranger(problems, answer=None):
    if len(problems) > 5:
         return'Error: Too many problems.'

    line_1 = ""
    line_2 = ""
    line_3 = ""
    line_4 = ""

    for i, problem in enumerate(problems):
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return'Error: Operator must be \'+\' or \'-\'.'
        if not (num1.isdigit() and num2.isdigit()):
             return'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4:
             return"Error: Numbers cannot be more than four digits."
        
        spaces_quantity = max(len(num1), len(num2)) + 2 #one space and one for operator
        if operator =="+":
            result = int(num1) + int(num2)
        else:
            result = int(num1) - int(num2)
        
        line_1 += num1.rjust(spaces_quantity)
        line_2 += operator +num2.rjust(spaces_quantity-1)
        line_3 += "-" * spaces_quantity
        line_4 += str(result).rjust(spaces_quantity)
        if i <len(problems)-1:
             line_1 += "    "
             line_2 += "    "
             line_3 += "    "
             line_4 += "    "
    if answer is True:
        arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3 + "\n" + line_4
    else:
        arranged_problems = line_1 + "\n" + line_2 + "\n" + line_3
    return arranged_problems
print(arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", ]))
