import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

dir = os.getcwd()

imgread = mpimg.imread(dir + '/image/piano-gf6c80237b_1920.jpg')[...,:3]
plt.imshow(imgread)
plt.show()

img_gray = np.dot(imgread,[0.299, 0.587, 0.144])
plt.imshow(img_gray, cmap=plt.get_cmap('gray'))
plt.show()