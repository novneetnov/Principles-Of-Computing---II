import simpleplot

counter = 0


def fib(num):
    global counter
    counter += 1
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num - 2)


#print fib(32)
#print counter


def memoized_fib(num, memo_dict = {0 : 0, 1 : 1}):
    global counter
    counter += 1
    if num in memo_dict:
        return memo_dict[num]
    else:
        sum1 = memoized_fib(num - 1, memo_dict)
        sum2 = memoized_fib(num - 2, memo_dict)
        memo_dict[num] = sum1 + sum2
        return sum1 + sum2

#print memoized_fib(50)
#print counter


def plot_example(length):
    global counter
    poly_func = []
    fib_func = []
    for iter in range(length):
        counter = 0
        poly_func.append([iter, 2 * iter - 1])
        answer = memoized_fib(iter, {0 : 0, 1 : 1})
        fib_func.append([iter, counter])
    simpleplot.plot_lines("Recurrence solutions", 600, 600, "number", "value", [poly_func, fib_func], legends = ["Ideal. Plot", "Fib plot"])

plot_example(10)