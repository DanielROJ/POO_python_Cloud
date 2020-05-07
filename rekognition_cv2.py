import boto3
import base64
import cv2
client = boto3.client('rekognition')




def use_label_detection():
    with  open('zorro.png','rb') as image:
        response = client.detect_labels(
            Image={
                'Bytes':b''+image.read(),
            },
            MaxLabels=10
        )
        print(response['Labels'][0]['Name'])
        pass

def use_text_detection():
    with open('placa2.png','rb') as placa:
        response = client.detect_text(
            Image={
                'Bytes': b''+placa.read(),
            },

        )
        print(response)
    pass

def use_detect_faces():
    with open('0.jpeg','rb') as face:
        response = client.detect_faces(
            Image={
                'Bytes': b''+face.read()
            },
            Attributes=[
                'ALL'
            ]
        )
        print(response)
    pass

def use_compare_faces():
    img_grupos = open('grupo_faces.jpeg','rb')
    img_sola = open('sola_face.jpeg','rb')
    response = client.compare_faces(
        SourceImage={
            'Bytes': b''+img_sola.read(),
        },
        TargetImage={
            'Bytes': b''+img_grupos.read(),
        },
        QualityFilter='HIGH'
    )
    box = response['FaceMatches'][0]['Face']['BoundingBox']
    im2 = cv2.imread('grupo_faces.jpeg')
    height, width, channels = im2.shape
    face = [( int(box['Left']*width),int( box['Top']*height),int(box['Width']*width), int(box['Height']*height))]
    print(face)
    for (x, y, w, h) in face:
        print((x, y, w, h))
        cv2.rectangle(im2, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', im2)
    cv2.waitKey()
    pass

#use_label_detection();
#use_detect_faces()
#use_text_detection()
#use_compare_faces()
