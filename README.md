# EagleView
Project: Binary Mask Creation

Overview:
    This project processes set of .jpg and .png images by creating a binary mask for each image and stores them.
    The binary mask identifies pixels where all 3 channels(i.e., RGB) have values above 200 (on an 8-bit scale).
    For each mask:
        Pixels meeting the condition (i.e., all channels are above 200) are marked as white (255).
        Pixels not meeting the condition are marked as black(0).

    along with mask creation will store the number of white pixel values in the current image. and will keep on sum up the count and at the end will show all the image white pixels count.

Features:
    Parallel processing: parallel processing is used to improve the performance when handling multiple images.
    handle varity of images: can able to handle the .jpg and .png images

Requirements versions:
    Python 3.12.2
    OpenCV library 4.5.5.64
    numpy 1.26.4

usage:
    1. run the activate.cmd -> it will activate the virtual environment and install the required dependeces.
        once the environment is activated place the required .jpg/.png image in the input folder
    2. Run the program
        python parallel_processing.py
            it will create the corresponding binsary masks for each image in the input folder and stores them in the output folder. and also the shows the output: count of max pixels across all images

Example:
    in the input folder already 3 input images are there. once the script is run it will create the masked images and stores them in the output folder with corresponding image name suffixed with _mask and prints the output: Total number of max pixels in all images: 23650


