import numpy as np
import pulp as p


# Create a LP Minimization problem 
Lp_prob = p.LpProblem('Problem', p.LpMinimize)  
  
# Create problem Variables  
#x = p.LpVariable("x", lowBound = 0)   # Create a variable x >= 0 
#y = p.LpVariable("y", lowBound = 0)   # Create a variable y >= 0 

x = p.LpVariable("x")
y = p.LpVariable("y")

# Prices 
S0 = 100 # Stock price (x)
# bond price is 1 it is the numerarie (y)
  
# Objective Function (minimize the portfolio value at the beginning)
Lp_prob += S0 * x + y    
  
# Constraints: 
u = 2
d = 1 / u

#Onfinanszirozas
Lp_prob += S0 * u * x + y = -100
Lp_prob += S0 * d * x + y = 0

# Nemnegativitasi feltetelek
Lp_prob += S0 * u * x + y >= 0
Lp_prob += S0 * d * x + y >= 0
  
# Display the problem 
print(Lp_prob) 
  
status = Lp_prob.solve()   # Solver 
print(p.LpStatus[status])   # The solution status 
  
# Printing the final solution 
print(p.value(x), p.value(y), p.value(Lp_prob.objective)) 
