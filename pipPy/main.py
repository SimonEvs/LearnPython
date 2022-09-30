# from isOdd import isOdd



# print(isOdd(0))
# print(isOdd(4)) 

# from progress.bar import Bar
# import time 

# bar = Bar('Processing', max=20)
# for i in range(20):
#     # Do some work
#     time.sleep(1)
#     bar.next()
# bar.finish()

# import emoji
# print(emoji.emojize('Python is :thumbs_up:'))
# print(emoji.emojize('Python is :thumbsup:', language='alias'))
# print(emoji.demojize('Python is 👍'))
# print(emoji.emojize("Python is fun :red_heart:"))
# print(emoji.emojize("Python is fun :red_heart:", variant="emoji_type"))
# print(emoji.is_emoji("👍"))

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# make data
x = np.arange(0, 10, 2)
ay = [1, 1.25, 2, 2.75, 3]
by = [1, 1, 1, 1, 1]
cy = [2, 1, 2, 1, 2]
y = np.vstack([ay, by, cy])

# plot
fig, ax = plt.subplots()

ax.stackplot(x, y)

ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
       ylim=(0, 8), yticks=np.arange(1, 8))

plt.show()