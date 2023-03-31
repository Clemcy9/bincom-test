import random
# dummy data 
data =[77, 78, 85, 86, 86, 86, 87, 87, 94, 98, 99, 103] 

# mean color of shirt
def mean_color(data):
    # temp variable to hold sum of all data
    total = 0

    # loop through data and get sum
    for x in data:
        total += x
    
    mean = total/len(data)
    return mean

# most worn throuhout the week ==mode
def mode_color(data):
    # dictionary to keep count of each number
    count ={}
    # loop through data, get counts of each number
    for x in data:
        if x in count:
            count[x] = count[x]+1
        else:
            count[x] = 1

    # sort the dictionary to get max number
    sort = sorted(count,reverse=True)
    return sort[0]

# median color, i.e most center number  or two most centerd nos divided by 2 in sort listed
def median_color(data):
    # sort data
    sort = sorted(data)
    data_length = len(sort)
    # variable to store median
    median = 0
    

    # return int(data_length/2)

    # check if list is even or odd
    if data_length % 2 != 0:
        
        median = sort[int(data_length/2)]
        return median
    else:
        median = (sort[int(data_length//2)] + sort[int(data_length//2 -1)])/2
        return median

# variance
def variance_color(data):
    # get mean
    m = mean_color(data)

    # For each value: find the difference from the mean:
    mean_dif = [x-m for x in data]
    # print(f'mean dif = {mean_dif}')

    # For each difference: find the square value:
    sq_mean_dif = [x*x for x in mean_dif]
    # print(f'sq mean dif = {sq_mean_dif}')

    # variance is the average number of these squared differences:
    variance = (sum(sq_mean_dif))/len(data)
    # print(f'variance = {variance}')
    return variance

def color_freq(data):
    count ={}
    # loop through data, get counts of each number
    for x in data:
        if x in count:
            count[x] = count[x]+1
        else:
            count[x] = 1
    return count

# convert from any base to base 10
def toBase10(num,base):
    num = str(num)
    sum=0
    for i in range(0,len(num)):
        sum+=int(num[i])*(base**(len(num)-(i+1)))
    return sum 

def rand_generator():
    num = random.randint(0,1)
    num_list_str = ''
    for i in range(0,2):
        num_list_str += str(random.randint(0,1))
    
    num_list_int = bytes(num_list_str,'utf-8')
    print(f'generated 4 random nos:{num_list_int}')

    value_in_10 =toBase10(num_list_str,2)
    return(value_in_10)
    

print(f'mean color shirt = {mean_color(data)}')
print(f'most worn color shirt = {mode_color(data)}')
print(f'median color shirt = {median_color(data)}')
print(f'variance = {variance_color(data)}')
print(f'color frequency = {color_freq(data)}')
print(f'random number to base 10 = {rand_generator()}')