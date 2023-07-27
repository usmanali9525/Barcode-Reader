import cv2
from pyzbar.pyzbar import decode

def decode_barcode(image):
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # Convert the image to grayscale for faster processing
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0) # Apply Gaussian blur to reduce noise (adjust the kernel size as needed)
    _, threshold_image = cv2.threshold(blurred_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # Apply Otsu thresholding to binarize the image
    barcodes = decode(threshold_image) # Find barcodes in the thresholded image
    barcodes = decode(gray_image) # Find barcodes in the image
    # Find barcodes in the image
    barcodes = decode(gray_image)
    
    # Process each barcode found
    if barcodes:
        barcode = barcodes[0]
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        x, y, w, h = barcode.rect
        return barcode_data, barcode_type, (x, y, w, h)
    
    else:
        return None, None, None

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        barcode_data, barcode_type, barcode_box = decode_barcode(frame)
        if barcode_data:
            print(f"Barcode Type: {barcode_type}")
            print(f"Barcode Data: {barcode_data}")

            x, y, w, h = barcode_box
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Save the captured frame with the barcode as an image
            cv2.imwrite("captured_image.png", frame)
            
            # Uncomment the following line if you want to stop the loop after detecting a barcode
            break
        
        cv2.imshow("Camera", frame)

        # Exit the loop when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
