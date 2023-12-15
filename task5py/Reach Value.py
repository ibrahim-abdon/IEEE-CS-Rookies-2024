# if the new value instead of 1 is bigger than the value we want to reach
# we can reach small number throught multiplication process

def reach_value(value, reach):
    if value == reach:
        return True
    if value > reach:
        return False
    return reach_value(value * 10, reach) or reach_value(value * 20, reach) 

    # new value will equal 10 OR 20 instead of 1
    # and will continue if equal yes else then it bigger and in this case no
    # بمعني هنفضل نعنل ريتيرن لحد متساويهم او تكون اكبر


test_number = int(input())
for index in range(test_number):
    n = int(input())
    result = reach_value(1, n)
    if result:
        print("YES")
    else:
        print("NO")
