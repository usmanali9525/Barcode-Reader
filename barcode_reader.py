import cv2
from pyzbar.pyzbar import decode

def load_image(image_path):
    return cv2.imread(image_path)

# Provide the image file path
image_path = "Images/datamatrix.png"
image = load_image(image_path)

def decode_barcode(image):
    
    #Preprocessing Images
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale for faster processing
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0) # Apply Gaussian blur to reduce noise (adjust the kernel size as needed)
    _, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Apply Otsu thresholding to binarize the image
    barcodes = decode(threshold_image) # Find barcodes in the thresholded image
    barcodes = decode(gray_image) # Find barcodes in the image
    
    # Process each barcode found
    for barcode in barcodes:
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        return barcode_data, barcode_type

    # If no barcode is found, return None
    return None, None

def main():

    barcode_data, barcode_type = decode_barcode(image)
    if barcode_data is not None:
        print(f"Barcode Type: {barcode_type}")
        print(f"Barcode Data: {barcode_data}")
    else:
        print("No barcode detected.")

if __name__ == "__main__":
    main()
