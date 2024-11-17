def divide_elements(values, divisor):
    result = []
    try:
        for value in values:
            r = value / divisor
            result.append(r)
    except ZeroDivisionError:
        print("Error : Division by zero is not possible")
        return
    except TypeError:
        print("Not Numeric")
        return
    return result
result = divide_elements([20,10,30,40],2)
print("Result: ",result)