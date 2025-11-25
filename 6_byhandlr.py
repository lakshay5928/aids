#linear regression by hand(without scikit learn)
import numpy as np
import matplotlib.pyplot as plt

# 1 dataset(x=study hour,y=marks)
x=np.array([1,2,3,4,5],dtype=float) #indepent variable
y=np.array([2,4,5,4,5],dtype=float) #dependent variable

# 2 compute mean
x_bar=np.mean(x)
y_bar=np.mean(y)

# 3 compute slope m and intercept c
numerator=np.sum(x-x_bar)*(y-y_bar)
denominator=np.sum((x-x_bar)**2)
m=numerator/denominator #slope
c=y_bar-m*x_bar #intercept

print("slope (m):",m)
print("intercept (c):",c)
print(f"equations of line: slopes={m}, intercepts={c}")

# 4 prediction and residuals
y_hat=m*x+c #prediction value
residuals=y-y_hat #errror

#5 evaluation (R2 and mse)
RSS=np.sum(residuals**2) #residual sum of squares
TSS=np.sum((y-y_bar)**2) #total sum of squares
R2=1-RSS/TSS #r2 score
MSE=RSS/len(y) #mean squared error

print("R2:",R2)
print("MSE:",MSE)

# 6 plot result
plt.scatter(x,y,label="Data points") #actual data
plt.plot(x,y_hat,color="red",label="Fitted line") #regresssion line
plt.xlabel("study hours")
plt.ylabel("marks")
plt.title("Linear Regression by Hand")
plt.legend()
plt.grid(True)
plt.show()