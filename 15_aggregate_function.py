import numpy as np
#Aggregate funvtion=summarize date and typically return a single value

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])
print(np.sum(array))
print(np.mean(array))#average
print(np.std(array))#standard deviation , statistic term
print(np.var(array))# standard deviation square
print(np.min(array))
print(np.max(array))
print(np.argmin(array))# position of the min value
print(np.argmax(array))# position of the max value
print(np.sum(array,axis=0)) # column sum     op:[ 7  9 11 13 15]
print(np.sum(array,axis=1)) #sum rows



'''
Other aggregate functions in NumPy include:

| Function             | Work                          |
| -------------------- | ----------------------------- |
| `np.median()`        | Middle value                  |
| `np.percentile()`    | Finds percentile              |
| `np.quantile()`      | Quantile calculation          |
| `np.average()`       | Weighted average possible     |
| `np.any()`           | True if any element is True   |
| `np.all()`           | True if all elements are True |
| `np.cumsum()`        | Cumulative sum                |
| `np.cumprod()`       | Cumulative product            |
| `np.ptp()`           | Range (max − min)             |
| `np.count_nonzero()` | Counts non-zero elements      |


'''


