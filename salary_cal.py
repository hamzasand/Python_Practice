working_hours =[int(x) for x in input(" Enter your working hours per day seperated by spaces ").split()] 
wage = int(input("Enter you hourly wega"))
total = sum(working_hours)
salary = total * wage

print(" Salary is ", salary)