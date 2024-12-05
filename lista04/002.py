import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np


img = mpimg.imread('/home/zegui/FPC/lista04/stinkbug.png')

img_height, img_width, tmp = img.shape
plt.imshow(img)
plt.axis("off")
num_spots = 20

for i in range(num_spots):
    x = np.random.randint(0, img_width)
    y = np.random.randint(0, img_height)

    radius = np.random.randint(5, 20)
    if(np.random.rand() > 0.5):
        color = (1, 1, 1)
    else:
        color = (0, 0, 0)
    
    circle = plt.Circle((x, y), radius, color=color, fill=True)
    plt.gca().add_patch(circle)

plt.show()
print(img.shape)
