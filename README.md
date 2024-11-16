# EagleView
**Project:** Binary Mask Creation

**Overview:**
This project processes a set of `.jpg`, `.jpeg` and `.png` images by creating a binary mask for each image and stores them. The binary mask identifies pixels where all three channels (RGB) have values above 200 (on an 8-bit scale).

- For each mask:
  - Pixels meeting the condition (i.e., all channels are above 200) are marked as white (255).
  - Pixels not meeting the condition are marked as black (0).
  - Along with mask creation, the program stores the number of white pixel values in the current image.
  - It sums up the count across all images and, at the end, displays the total count of white pixels.

**Features:**
- **Parallel processing:** Used to improve performance when handling multiple images.
- **Handles a variety of images:** Supports variety image formats `.jpg`, `.jpeg` and `.png` formats.

**Requirements:**
- Python 3.12.2
- OpenCV library 4.5.5.64
- numpy 1.26.4

**Building the Project:**
1. Run `activate.cmd`
   - This will activate the virtual environment and install the required dependencies.
   - Once the environment is activated, place the required `.jpg`/`.png` images in the `input_data` folder.

2. Run the program
   ```bash
   python parallel_processing.py

Example:
    In the input_data folder already 3 input images are there. once the script is run it will create the masked images and stores them in the output_data folder with corresponding image names suffixed with `_mask` and prints the output: `Total number of max pixels in all images: 23650`