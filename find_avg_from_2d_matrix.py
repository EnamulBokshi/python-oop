import numpy as np
def find_avg(students):
    avg = np.mean(students,axis=1)
    mean_index = np.argmax(avg)
    highest = avg[mean_index]
    print(f"Student: {mean_index+1}\nAverage Mark: {highest}")
students = np.array([
    [80,90,23,60],
    [80, 90, 23, 40],
    [55, 30, 23, 70],
    [77, 95, 23, 60],
    [99, 20, 23, 50]
])
find_avg(students)

