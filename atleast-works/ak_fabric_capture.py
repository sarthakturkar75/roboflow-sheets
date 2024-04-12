import cv2
from tkinter import *
from PIL import Image, ImageTk
import os

# Set the output folder
output_folder = "C:\\Users\\sarth\\Pictures\\sheet"
os.makedirs(output_folder, exist_ok=True)

# Create the main window
root = Tk()
root.title("Real-time Image Capture")

# Create a label to display the image
label = Label(root)
label.pack(padx=10, pady=10)

# Create a function to capture and display the image
def capture_image():
    # Open the default camera (index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Unable to open camera.")
        return

    # Counter for image filenames
    image_count = 0

    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame from BGR to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Convert the frame to a PhotoImage
        photo = ImageTk.PhotoImage(image=Image.fromarray(rgb_frame))

        # Update the label with the new image
        label.configure(image=photo)
        label.image = photo

        # Save the frame as an image file without color conversion
        image_filename = os.path.join(output_folder, f"image_{image_count}.png")
        cv2.imwrite(image_filename, frame)
        image_count += 1

        # Update the main window
        root.update()

        # Break the loop if the user closes the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the OpenCV window
    cap.release()
    cv2.destroyAllWindows()

# Create a button to start capturing images
start_button = Button(root, text="Start Capture", command=capture_image)
start_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()
