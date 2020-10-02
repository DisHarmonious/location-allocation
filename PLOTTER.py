import numpy as np
import matplotlib.pyplot as plt

##### QUESTION 1
n_groups = 3

wogp = (1320.48, 210.99, 159.98)

wgp = (53.70, 50.98, 50.60)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Radius')
plt.ylabel('Time (s)')
plt.title('Time consumed for question 1')
plt.xticks(index + bar_width / 2, ('R=1', 'R=5', 'R=10'))
plt.legend()

plt.tight_layout()
plt.show()

##### EFFICIENCY QUESTION 1
n_groups = 3

wogp = (9547, 14156, 14307)

wgp = (5894756, 145242271, 411204566)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Radius')
plt.ylabel('Quantity')
plt.title('Number of Restaurants counted for question 1')
plt.xticks(index + bar_width / 2, ('R=1', 'R=5', 'R=10'))
plt.legend()

plt.tight_layout()
plt.show()

##### EFFICIENCY QUESTION 2
n_groups = 3

wogp = (14369, 14369, 14369)

wgp = (21012, 34430, 67180)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('k nearest')
plt.ylabel('Quantity')
plt.title('Number of Restaurants counted for question 2')
plt.xticks(index + bar_width / 2, ('k=3', 'k=5', 'k=10'))
plt.legend()

plt.tight_layout()
plt.show()


##### QUESTION 2
n_groups = 3

wogp = (310.60, 184.26, 92.36)

wgp = (50.91, 51.32, 49.55)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('k Nearest Restaurants')
plt.ylabel('Time (s)')
plt.title('Time consumed for question 2')
plt.xticks(index + bar_width / 2, ('k=3', 'k=5', 'k=10'))
plt.legend()

plt.tight_layout()
plt.show()


###################### SCALABILITY #####################
### for Q1
n_groups = 3

wogp = (20.18, 96.12, 210.99)

wgp = (2.41, 20.37, 50.98)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Dataset Length')
plt.ylabel('Time (s)')
plt.title('Scalability for question 1, R=5')
plt.xticks(index + bar_width / 2, ('l=250', 'l=2500', 'l=25000'))
plt.legend()

plt.tight_layout()
plt.show()


### for Q2
n_groups = 3

wogp = (28.41, 174.34, 184.26)

wgp = (2.22, 20.48, 51.32)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Dataset Length')
plt.ylabel('Time (s)')
plt.title('Scalability for question 2, k=5')
plt.xticks(index + bar_width / 2, ('l=250', 'l=2500', 'l=25000'))
plt.legend()

plt.tight_layout()
plt.show()


############# TOTAL TIME CONSUMED #############
# 12452.58
# 5796.86 - 2355.28
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(
    [12452.58, 5796.86, 2355.28],
    index = ['no Grid', 'Build+Test Grid', 'Test w/ Grid']
)
plt.title("Total Time Taken for testing")
plt.ylabel('Time Consumed (s)')
plt.xlabel('Method')

ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

my_colors = 'rbb'  #red, green, blue, black, etc.

s.plot( 
    kind='bar', 
    color=my_colors,
    rot=0
)
plt.show()

############# increase grid efficiency #############
#17993.58
#15360.21
#3011.34
import pandas as pd
import matplotlib.pyplot as plt

s = pd.Series(
    [17993.58, 15360.21, 3011.34],
    index = ['Brute Force', 'use of Break', 'Break+Horizontal Access']
)
plt.title("Time Taken for Grid Partition")
plt.ylabel('Time Consumed (s)')
plt.xlabel('Method')

ax = plt.gca()
ax.tick_params(axis='x', colors='blue')
ax.tick_params(axis='y', colors='red')

my_colors = 'rgb'  #red, green, blue, black, etc.

s.plot( 
    kind='bar', 
    color=my_colors,
    rot=0
)
plt.show()


#q3 scalability
n_groups = 3

wogp = (50.19, 501.53, 2714.66)

wgp = (7.28, 77.34, 731.22)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Dataset Length')
plt.ylabel('Time (s)')
plt.title('Scalability for question 3, R=5')
plt.xticks(index + bar_width / 2, ('l=250', 'l=2500', 'l=25000'))
plt.legend()

plt.tight_layout()
plt.show()

#q3 time
n_groups = 3

wogp = (3948.77, 2932.50, 2975.11)

wgp = (797.88, 784.71, 774.51)

fig, ax = plt.subplots()

index = np.arange(n_groups)
bar_width = 0.35

opacity = 0.4

rects1 = plt.bar(index, wogp, bar_width,
                 alpha=opacity,
                 color='b',
                 label='without Grid Partition')

rects2 = plt.bar(index + bar_width, wgp, bar_width,
                 alpha=opacity,
                 color='r',
                 label='with Grid Partition')

plt.xlabel('Radius')
plt.ylabel('Time (s)')
plt.title('Time Consumed for question 3')
plt.xticks(index + bar_width / 2, ('R=1', 'R=5', 'R=10'))
plt.legend()

plt.tight_layout()
plt.show()
