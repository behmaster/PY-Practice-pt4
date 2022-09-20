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

triangle = [[1],[1,1]]
def pascal(n):
    #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate numbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(15)