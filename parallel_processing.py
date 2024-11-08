import cv2 as cv
import numpy as np
import os
from glob import glob
from concurrent.futures import ThreadPoolExecutor, as_completed

input_dir = 'input_data'
output_dir = 'output_data'

os.makedirs(output_dir, exist_ok=True)

def applyMask(file_path):
    image = cv.imread(file_path)

    if image is None:
        print(f"Failed to read the image: {file_path}")
        return 0

    # Create a binary mask where all 3 channels pixel values are above 200
    mask = cv.inRange(image, (200, 200, 200), (255, 255, 255))

    # number of max-value pixels in the image
    No_of_Max_Pixels_in_Image = np.sum(mask == 255)

    # Save the mask
    imageName = os.path.basename(file_path)
    maskName = os.path.basename(file_path).split(".")[0] + "_mask." + os.path.basename(file_path).split(".")[1]
    output_path = os.path.join(output_dir, maskName)
    
    # write out the masked image
    cv.imwrite(output_path, mask)

    # return the max_pixel count of the particular image
    return No_of_Max_Pixels_in_Image

def main():
    # Define the list of allowed image formats for masking
    image_formats = ['.jpg', '.png', '.jpeg']

    # Get list of all files in the input directory which follow the image formats mentioned
    total_files = [
        file for file in glob(os.path.join(input_dir, "*"))
        if os.path.splitext(file)[1].lower() in image_formats
    ]

    total_max_pixel_count = 0

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(applyMask, file_path) for file_path in total_files]
        
        for future in as_completed(futures):
            # add max pixel count of each image
            total_max_pixel_count += future.result()

    # print total number of max pixels in all images
    print(f"Total number of max pixels in all images: {total_max_pixel_count}")

if __name__ == '__main__':
    main()
