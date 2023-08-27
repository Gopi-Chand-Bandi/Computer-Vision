import cv2
def detect_face(image_path):
    # Load the face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Read and convert the image to grayscale
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.1, minNeighbors=5)

    # Assuming there's only one face in the image, return its coordinates
    if len(faces) == 1:
        return faces[0]
    else:
        return None

def main():
    # Paths to the input images
    image_path_1 = 'C:/Users/91817/Downloads/project/pkbandw.jpeg'
    image_path_2 = 'C:/Users/91817/Downloads/project/slbandw.jpeg'

    # Detect the face in the second image
    face_coords_2 = detect_face(image_path_2)
    if face_coords_2 is None:
        print("No face found in the second image.")
        return
    
    face_coords_1 = detect_face(image_path_1)
    if face_coords_1 is None:
        print("No face found in the First image.")
        return
    
    #Get Co-ordinates of First Image
    image1=cv2.imread(image_path_1)
    face_width_1,face_height_1 = face_coords_1[2], face_coords_1[3]
    extracted_image1=image1[face_coords_1[1]:face_coords_1[1] + face_height_1, face_coords_1[0]:face_coords_1[0] + face_width_1]

    #Get Co-ordinates of Second Image
    image2=cv2.imread(image_path_2)
    face_width_2,face_height_2 = face_coords_2[2], face_coords_2[3]
    extracted_image2=image2[face_coords_2[1]:face_coords_2[1] + face_height_2, face_coords_2[0]:face_coords_2[0] + face_width_2]

    extracted_image1_resized = cv2.resize(extracted_image1, (face_width_2, face_height_2))
    extracted_image2_resized = cv2.resize(extracted_image2, (face_width_1, face_height_1))
    
    # Place the extracted images on each other's images at the specified positions
    image1[face_coords_1[1]:face_coords_1[1] + face_height_1, face_coords_1[0]:face_coords_1[0] + face_width_1] = extracted_image2_resized
    image2[face_coords_2[1]:face_coords_2[1] + face_height_2, face_coords_2[0]:face_coords_2[0] + face_width_2] = extracted_image1_resized

    cv2.imshow('Swapped Image 1', image1)
    cv2.imshow('Swapped Image 2', image2)


    # # Load and resize the source face
    # image_1 = cv2.imread(image_path_1)
    # face_width, face_height = face_coords_2[2], face_coords_2[3]
    # image_1_resized = cv2.resize(image_1, (face_width, face_height))

    # # Extract the target face region from the second image
    # image_2 = cv2.imread(image_path_2)
    # roi = image_2[face_coords_2[1]:face_coords_2[1] + face_height, face_coords_2[0]:face_coords_2[0] + face_width]

    # # Flip the target face horizontally
    # reflected_roi = cv2.flip(roi, 1)

    # # Blend the two faces together
    # alpha = 0.7
    # blended_image = cv2.addWeighted(image_1_resized, alpha, reflected_roi, 1 - alpha, 0)

    # # Replace the target face region with the blended image
    # image_2[face_coords_2[1]:face_coords_2[1] + face_height, face_coords_2[0]:face_coords_2[0] + face_width] = blended_image

    # # Display the result
    # cv2.imshow('Blended Image', image_2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
