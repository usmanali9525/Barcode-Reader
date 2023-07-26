import cv2
from pyzbar.pyzbar import decode

def decode_barcode(image):
    # Convert the image to grayscale for faster processing
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Find barcodes in the image
    barcodes = decode(gray_image)
    
    # Process each barcode found
    if barcodes:
        barcode = barcodes[0]
        barcode_data = barcode.data.decode('utf-8')
        barcode_type = barcode.type
        return barcode_data, barcode_type
    else:
        return None, None

def main():
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        barcode_data, barcode_type = decode_barcode(frame)
        if barcode_data:
            print(f"Barcode Type: {barcode_type}")
            print(f"Barcode Data: {barcode_data}")

            # Save the captured frame with the barcode as an image
            cv2.imwrite("captured_image.png", frame)
            
            # Uncomment the following line if you want to stop the loop after detecting a barcode
            # break
        
        cv2.imshow("Camera", frame)

        # Exit the loop when the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
