# import cv2
# import numpy as np
# from pyzbar.pyzbar import decode

# def decoder(image):
#     gray_img = cv2.cvtColor(image,0)
#     barcode = decode(gray_img)

#     for obj in barcode:
#         points = obj.polygon
#         (x,y,w,h) = obj.rect
        # pts = np.array(points, np.int32)
        # pts = pts.reshape((-1, 1, 2))
        # cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        # barcodeData = obj.data.decode("utf-8")
        # barcodeType = obj.type
        # string = "Data " + str(barcodeData) + " | Type " + str(barcodeType)
        
        # cv2.putText(frame, string, (x,y), cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,0,0), 2)
        # print("Barcode: "+barcodeData +" | Type: "+barcodeType)

# cap = cv2.VideoCapture(0)
# while True:
#     try:
#         ret, frame = cap.read()
#         decoder(frame)
#         cv2.imshow('Image', frame)
#         code = cv2.waitKey(10)
#         if code == ord('q'):
#             break
#     except Exception as er:
#         with open("error.txt", 'w+') as f:
#             f.write(str(er))

# importing required libraries
def check_if_id(id):
        id = id.split('_')
        if len(id) == 2:
            if id[1].isdigit():
                return True
        return False