def max_num(x,y,z=0):
    return max([x,y,z])
print("The output of max_num(2,50,14) is:")
print(max_num(2,50,14)) 


def mult_list(lst):
    product = lst[0]
    if len(lst) > 1:
        for i in lst[1:]:
            product = product * i
    return product
print("The output of mult_list([10,2,.5]) is:")
print(mult_list([10,2,.5]))


def rev_string(string):
    return string[::-1]
print("The output of rev_string('Hello World') is:")
print(rev_string("Hello World"))

def num_within(number,beg_range,end_range):
    return number in range(beg_range,end_range)
print("The output of num_within(2,1,3) is:")
print(num_within(5,1,3))

def pascal():