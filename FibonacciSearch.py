#Example Equation
#equation = (x**4) - (14*(x**3)) + (60*(x**2)) - (70*x)


#Getting the value of the equation
def eqn(x):
    equation = (x**4) - (14*(x**3)) + (60*(x**2)) - (70*x)
    return equation


#creating a list with N+1 fibonacci numbers
def fibonacci(n):
    first = 1
    second =1
    fib = [1,1]
    if n<=2:
        return fib
    
    for i in range(n):
        third = first+second
        fib.append(third)
        first,second = second,third

    return fib


#Creating a list containing p1,p2,....pN
def p_list(n):
    
    p=[0]

    for k in range(1,n+1):
        p_temp = 1 - (fib[n-k+1]/fib[n-k+2])
        p.append(p_temp)

    return p


#Calculation for N iterations
def iterations(n):
    global start,end
    start1 = start
    end1 = end

    for i in range(1,n+1):
        start1 = start + (p[i]*(end-start))
        end1 = start + ((1-p[i])*(end-start))

        f_start = eqn(start1)
        f_end = eqn(end1)

        if f_start<f_end:
            end = end1
        else:
            start = start1
        print(f"Iteration {i}:",[start,end])


#The equation in use
print("x^4 - 14x^3 + 60x^2 - 70x")

        
#No. of Iterations
n = int(input("Enter the no. of iterations: "))
    
#Defining the range [0,2]
start = float(input("Enter the range start: "))
end = float(input("Enter range end: "))

fib = fibonacci(n)
p = p_list(n)

iterations(n)



#Plotting the graph to visualize the equation
#Please install the following libraries before proceeding with the code below: matplotlib, numpy
# import matplotlib.pyplot as plt
# import numpy as np
 

# x = np.linspace(start, end,10)
# y = (x**4) - (14*(x**3)) + (60*(x**2)) - (70*x)
# fig = plt.figure(figsize = (10, 5))
# plt.plot(x, y)
# plt.show()
