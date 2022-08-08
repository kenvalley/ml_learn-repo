# AI School Simulation codes - Week 1

# Section 2: Predicting the Movie Box Office Revenue with Linear Regression

# Import Libraries
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Read data from system. This is the reference data
data = pd.read_csv('cost_revenue_clean.csv')

# Create dependent and independent variables 
X = DataFrame(data, columns = ['production_budget_usd'])
y = DataFrame(data, columns = ['worldwide_gross_usd'])

# Scatter plot generated from the data with appropriate labels 
plt.figure(figsize=(10,6))
plt.scatter(X,y, alpha = 0.4)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Producton Budget $')
plt.xlim(0, 0.45e9)
plt.ylim(0,3e9)
plt.show()

# Create an object named 'regress' and fit to our regressor
regress = LinearRegression()
regress.fit(X,y)

# Code to show slope coefficient and intercept
regress.coef_ #theta_1
regress.intercept_ #

# Plot the linear regression line and the scatter plot on same figure
plt.figure(figsize=(10,6))
plt.scatter(X,y, alpha = 0.4)
plt.plot(X, regress.predict(X), color='red', linewidth=4)
plt.title('Film Cost vs Global Revenue')
plt.xlabel('Producton Budget $')
plt.xlim(0, 0.45e9)
plt.ylim(0,3e9)
plt.show()

# Measure of goodness of fit
regress.score(X,y)



########################################################################################
########################################################################################
########################################################################################
# Section 3: Python programming for Data Science and Machine Learning

# Working with variables, list, the 'type' function and the 'sort' function
a = 5
b = 10
prime_numbers = [1,4,5,7,7]
type(prime_numbers)
scores = [43, 12, 6, 78, 2, 14]
top_scores = []
scores.sort(reverse=True)
scores[0:3]


# Read our csv file and save it to the variable named 'data'. This is possible because we already imported 'pandas'
data = pd.read_csv('lsd_math_score_data.csv')

# Manipulating our DataFrame; print out, check type, print out a particular column (via column name, instead of index)
only_math_scores = data['Avg_Math_Test_Score']

# Setting the values of a particular column
data['High_Score'] = '302

# Overwrite the values stored in a particular column to equal the original value + something else
data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']'

# Delete a column 
del data['LSD_ppm']

# Introduction to functions in Python; the code below is a function to get milk from a store
def get_milk():
    print('Open door')
    print('Go to the shop')
    print('Buy milk')
    print('Come back home')
    

# My solution to coding exercise - part 1
tracker = 0

def moveForwards():
    global tracker 
    tracker += 1
    print('moved forward by one step.')

def turnRight():
    global tracker
    tracker -= 1
    print('turning right')
    
def move():
    #Delete this line and replace with your code. 
    moveForwards()
    turnRight()
    turnRight()
    turnRight()
    moveForwards()
    turnRight()
    turnRight()
    turnRight()
    moveForwards()
    turnRight()
    moveForwards()
    turnRight()
    moveForwards()
    moveForwards()
    
    return tracker
  
# Include multiple arguments for the function; Inputs and Parameters
def get_milk_again(amount, destination):
    print('Open door')
    print('Go to ' + destination)
    print('Buy ' + str(amount) + ' milk')
    print('Come back home')

# Calling the function
get_milk_again(30, "mama's shop")

# Concatenating lists
concatenate_lists(['a', 'b', 'c'], [1,2,3])

# Data visualization with Python

#1.
plt.title('Title of our graph', fontsize=17)
plt.xlabel("Time in mins", fontsize=14)
plt.ylabel("Tissue LSD ppm", fontsize=14)
plt.text(x=0, y=35,s='ERE!')
plt.plot(time, avg_mth)
plt.xticks(fontsize=14)

#2.
%matplotlib inline

plt.style.use('fivethirtyeight')
plt.scatter(LSD, score, color='g', s=100, alpha=0.9)
plt.title('Arithmetic vs LSD-25', fontsize=14)
plt.xlabel('Tissue LSD ppm', fontsize=14)
plt.ylabel('Performance Score', fontsize=17)
plt.ylim(25, 85)
plt.xlim(1,6.7)
plt.plot(LSD, predict, color='r', linewidth=4)

#### END ####################################################
