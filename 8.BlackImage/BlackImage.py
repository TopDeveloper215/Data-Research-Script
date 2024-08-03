import cv2
import os
import numpy as np

def simulate_night_vision(image):
    # Convert to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Apply gamma correction to enhance the image (adjust gamma value as needed)
    gamma = 0.2

    gamma_corrected = np.power(gray_image / 255.0, gamma) * 255.0
    gamma_corrected = gamma_corrected.astype(np.uint8)
    
    # Apply contrast enhancement
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    enhanced_image = clahe.apply(gamma_corrected)
    
    return enhanced_image

def apply_thermal_effect(image):
    # Apply a thermal effect using a colormap
    thermal_image = cv2.applyColorMap(image, cv2.COLORMAP_JET)
    
    # Convert to grayscale
    thermal_gray = cv2.cvtColor(thermal_image, cv2.COLOR_BGR2GRAY)
    
    # Normalize the image to enhance the contrast
    thermal_bw = cv2.normalize(thermal_gray, None, 0, 255, cv2.NORM_MINMAX)
    
    return thermal_bw

def process_folder(input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Process each image in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
            
            # Read the image
            image = cv2.imread(input_path)
            
            # Simulate night vision
            night_vision_image = simulate_night_vision(image)
            
            # Apply thermal effect
            thermal_bw_image = apply_thermal_effect(night_vision_image)
            
            # Save the result
            cv2.imwrite(output_path, thermal_bw_image)
            print(f"Processed {filename}")

# Example usage
current_dir = os.path.dirname(os.path.abspath(__file__))
input_folder = os.path.join(current_dir, 'input')
output_folder = os.path.join(current_dir, 'output')

# Create input and output directories if they do not exist
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Process the folder
process_folder(input_folder, output_folder)

print(f"All images in '{input_folder}' have been processed and saved to '{output_folder}'")
