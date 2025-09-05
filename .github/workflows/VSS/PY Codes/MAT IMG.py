import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("PreSub.png")
plt.imshow(img)
plt.axis('off')  # Hides the axis
plt.show()
