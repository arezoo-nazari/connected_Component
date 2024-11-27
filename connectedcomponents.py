import cv2
import numpy as np
# Read the input image (make sure it's a binary image)
image = cv2.imread('persian-digits.jpg', cv2.IMREAD_GRAYSCALE)
# Apply thresholding to create a binary image
_, binary_image = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
binary_image = 255-binary_image
# Use connectedComponentsWithStats to obtain labels and bounding boxes
num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(binary_image, connectivity=8)
# Iterate through each connected component
for label in range(1, num_labels):
    # Get the bounding box of the current connected component
    x, y, w, h = stats[label][:4]
    # Crop the connected component using the bounding box
    connected_component = image[y:y+h, x:x+w]
    
    # Display or save the cropped connected component
    cv2.imshow(f'Cropped Component {label}', connected_component)
    cv2.waitKey(0)
    cv2.destroyAllWindows()