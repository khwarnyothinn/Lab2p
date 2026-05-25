
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average(num_list)
    calc_max_min_temperature(num_list)
    calc_median_temperature(num_list)
    
def display_main_menu():
    print("Enter some numbers separated by commas (eg. 5,67, 32)")

def get_user_input():
    number = input()
    x = number.split(",")
    x = [int(num) for num in x]
    print(x)
    return x

def calc_average(num_list):
    total = sum(num_list)
    average = total/len(num_list)
    print("Average temperature: "+ str(average))
    return average

def calc_max_min_temperature(num_list):
    maximum = max(num_list)
    minimum = min(num_list)
    print("Maximum temperature: " + str(maximum))
    print("Minimum temperature: " + str(minimum))

def calc_median_temperature(num_list):
    sortnum = sorted(num_list)
    n = len(sortnum)
    if n % 2 == 1:
        median = sortnum[ n //2 ]
    else:
        median = (sortnum[(n//2)- 1] + sortnum[n // 2])/ 2

    print("Median temperature: " + str(median))
    return median

if __name__=="__main__":
    main()