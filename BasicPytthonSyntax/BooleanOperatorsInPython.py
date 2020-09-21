"""

Truth table for 'And'
**************************************
True and True   --> True
True and False  --> False
False and False --> False
**************************************

Truth table for 'Or'
**************************************
True or True   --> True
True or False  --> True
False or False --> False
**************************************

Truth table for 'Not'
**************************************
Not True  --> False
Not False --> True
"""

and_output1 = (10 == 10) and (10 > 9)
and_output2 = (10 == 10) and (10 < 9)
and_output3 = (10 > 10) and (10 < 9)

or_output1 = (10 == 10) or (10 > 9)
or_output2 = (10 == 10) or (10 < 9)
or_output3 = (10 > 10) or (10 < 9)

not_true = not (10 == 10)
not_false = not (10 > 10)

print(not_false)

"""
Comparators
== --> Value Equality
!= --> Not equal to
< --> Less than
> --> Greater than
<= --> Less than or equal to
>= --> Greater than or equal to
"""

bool_one = 10 == 11
not_equal = 10 != 11
less_than = 10 < 11
greater_than = 10 > 9
lt_eq = 10 <= 10
gt_eq = 10 >= 11 - 1
print(gt_eq)

"""
Precedence order is
1. not
2. and
3. or
"""

bool_output = True or not False and False
#  True
print(bool_output)

bool_output_1 = (10 == 10 or not 10 > 10) and 10 > 10
# True or True -> True and False -> False
print(bool_output_1)
