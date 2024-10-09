from PIL import Image
import os

def jpeg_to_png_converter():
    print("Welcome to the JPEG to PNG Converter")

    while True:
        # Read JPEG file
        jpeg_path = input("Enter the path to your JPEG file: ")
        
        if not os.path.exists(jpeg_path):
            print("Error: File not found. Please ensure the path is correct.")
            continue

        try:
            # Open the JPEG file
            with Image.open(jpeg_path) as img:
                # Convert to PNG
                png_path = os.path.splitext(jpeg_path)[0] + ".png"
                
                # Write PNG file
                img.save(png_path, "PNG")
                
                print(f"Conversion successful. PNG file saved as: {png_path}")
        except Exception as e:
            print(f"Error: An error occurred during conversion: {str(e)}")
            continue

        # Ask if the user wants to convert another file
        another = input("Do you want to convert another file? (yes/no): ").lower()
        if another != 'yes':
            break

    print("Thank you for using the JPEG to PNG Converter. Goodbye!")

# Run the converter
if __name__ == "__main__":
    jpeg_to_png_converter()
