import cv2
import os

# Set low & high thresholds for Canny edge detection
def canny_edge_detection(input_folder, output_folder, low_threshold=50, high_threshold=150):
    try:
        # Create output folder if it doesn't exist
        os.makedirs(output_folder, exist_ok=True)

        # Loop through all image files in the input folder
        for filename in os.listdir(input_folder):
            if filename.lower().endswith(('.png', '.jpg', '.webp')):
                input_path = os.path.join(input_folder, filename)
                output_path = os.path.join(output_folder, filename)

                # Read the image
                image = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)

                # Apply Gaussian blur to reduce noise and improve edge detection
                blurred = cv2.GaussianBlur(image, (5, 5), 0)

                # Apply Canny edge detection
                edges = cv2.Canny(blurred, low_threshold, high_threshold)

                # Save the result
                cv2.imwrite(output_path, edges)
                print(f"Canny edge detection applied. Result saved to {output_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_folder_path = r"C:\Users\User\Desktop\Example_Folder"  # Replace with your input folder path
    output_folder_path = r"C:\Users\User\Desktop\Example_Folder\canny_output"  # Replace with desired output folder path

    canny_edge_detection(input_folder_path, output_folder_path)