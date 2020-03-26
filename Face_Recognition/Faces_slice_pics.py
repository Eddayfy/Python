from PIL import Image
import face_recognition

image = face_recognition.load_image_file("1.jpg")   #image

face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

for face_location in face_locations:

    top, right, bottom, left = face_location

    face_image = image[top:bottom, left:right]
    pil_image = Image.fromarray(face_image)
    pil_image.save("face_img1.png")