from PIL import Image
import os

def resize_image_to_target_size(input_path, output_path, target_size_kb=1024):
    """
    Resizes an image to ensure its size is below the target size (in KB).
    
    Parameters:
        input_path (str): Path to the input image file.
        output_path (str): Path to save the resized image.
        target_size_kb (int): Target file size in kilobytes (default is 1024 KB).
    """
    with Image.open(input_path) as img:
        # Get the original dimensions
        width, height = img.size

        # Set an initial quality and scale factor
        quality = 95
        scale_factor = 1.0
        
        while True:
            # Resize the image
            new_width = int(width * scale_factor)
            new_height = int(height * scale_factor)
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Save the image with adjusted quality
            resized_img.save(output_path, format=img.format, quality=quality)
            
            # Check the file size
            file_size_kb = os.path.getsize(output_path) / 1024
            if file_size_kb <= target_size_kb or scale_factor <= 0.1:
                break  # Stop if the file size is within the limit
            
            # Adjust the scale factor and quality for further reduction
            scale_factor *= 0.9
            quality = max(10, quality - 5)  # Avoid reducing quality below 10
            
        print(f"Resized image saved to {output_path}, size: {file_size_kb:.2f} KB")

# Example usage
input_image_path = r"C:\Users\Demir\Downloads\IMG_3221.jpeg"
output_image_path = r"C:\Users\Demir\Documents\my_image_resized.jpg"  # Save here

resize_image_to_target_size(input_image_path, output_image_path)
