import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("Libraries/Pictures/Prub.png")
plt.imgshow(img)
plt.axis('off')  # Hides the axis
plt.show()
