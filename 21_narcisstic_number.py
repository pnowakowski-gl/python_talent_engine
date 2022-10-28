def narcissistic(test_number):
    length = len(str(test_number))
    return test_number == sum([int(i) ** length for i in str(test_number)])


print(narcissistic(7))  # True
print(narcissistic(371))  # True
print(narcissistic(122))  # False
print(narcissistic(4887))  # False
print(
    narcissistic(
        1891239131982312938123123134234234234234235423414235453566758578567564645646568464453453635656456234243243499999999999
    )
)
