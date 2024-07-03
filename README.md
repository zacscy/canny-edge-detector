##Canny Edge Detection Script
#Overview

This script performs Canny edge detection on all images in a specified input folder and saves the processed images to an output folder. The Canny edge detection algorithm highlights the edges in the images, which can be useful for various image processing tasks.
Requirements

    Python 3.x
    OpenCV (cv2)
    OS module

Installation

    Install Python from python.org.
    Install OpenCV by running the following command:

    sh

    pip install opencv-python

Usage

    Place your images in the input folder.

    Modify the input_folder_path and output_folder_path variables in the script to point to your desired input and output directories.

    Run the script using Python.

    sh

    python script_name.py

Script Parameters

    input_folder: The directory containing the images to be processed.
    output_folder: The directory where the processed images will be saved.
    low_threshold (default: 50): The lower boundary for the hysteresis procedure in the Canny edge detection.
    high_threshold (default: 150): The upper boundary for the hysteresis procedure in the Canny edge detection.

Example Usage

To use this script, replace the example paths with your actual paths:

python

if __name__ == "__main__":
    input_folder_path = r"C:\Users\User\Desktop\Example_Folder"  # Replace with your input folder path
    output_folder_path = r"C:\Users\User\Desktop\Example_Folder\canny_output"  # Replace with desired output folder path

    canny_edge_detection(input_folder_path, output_folder_path)

Modifying Parameters
How to Change Parameters

You can change the low_threshold and high_threshold parameters by passing them as arguments to the canny_edge_detection function. These thresholds control the sensitivity of the edge detection process.

For example:

python

canny_edge_detection(input_folder, output_folder, low_threshold=30, high_threshold=100)

Effects of Parameters

    Low Threshold (low_threshold): Pixels with a gradient intensity lower than this value will be rejected. Increasing this value will result in fewer edges being detected, potentially ignoring weak edges.
    High Threshold (high_threshold): Pixels with a gradient intensity higher than this value will be considered as edges. Decreasing this value will result in more edges being detected, potentially including noise as edges.

Choosing Thresholds

Choosing appropriate threshold values depends on the specific characteristics of your images and the desired outcome. Generally, you may need to experiment with different values to achieve the best results.
Example Output

After running the script, the output folder will contain images processed with Canny edge detection, saved with the same filenames as the original images. You can view these images to see the detected edges.
Error Handling

The script includes basic error handling to catch and display any errors that occur during execution. If an error occurs, it will be printed to the console.
License

This script is provided under the MIT License. Feel free to use and modify it as needed.
Contributing

If you have any suggestions or improvements, feel free to submit a pull request or open an issue on the GitHub repository.
