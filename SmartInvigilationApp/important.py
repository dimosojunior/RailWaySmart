
AWS Terminal
https://eu-north-1.console.aws.amazon.com/ec2-instance-connect/ssh?connType=standard&instanceId=i-051b0c1f9b69d5bb4&osUser=ec2-user&region=eu-north-1&sshPort=22#/


To Connect to the Terminal
https://eu-north-1.console.aws.amazon.com/ec2/home?region=eu-north-1#ConnectToInstance:instanceId=i-051b0c1f9b69d5bb4



BBOX_

[[-76.825165 345.9478    87.617516 547.3037  ]
 [302.04672  163.34067  380.0983   259.25977 ]
 [120.40265  130.62308  186.46005  210.27997 ]]

LANDMARKS_

[[[-34.039093   421.1461    ]
  [ 16.470798   427.12183   ]
  [-35.07744    464.84344   ]
  [-41.21428    498.56042   ]
  [ -0.88659286 504.5458    ]]

 [[324.0439     198.46864   ]
  [360.09473    200.7623    ]
  [339.04395    216.24658   ]
  [324.7361     238.5289    ]
  [353.1474     240.4968    ]]

 [[133.74072    161.84549   ]
  [163.7682     158.71199   ]
  [145.17691    176.29892   ]
  [138.92558    193.42422   ]
  [164.13974    191.53346   ]]]

 PROB_
 [0.9998667 0.9999882 0.9963965]




angle_R_List = [41.499546, 38.9971]
angle_L_List= [44.377758, 45.907673]
predLabelList= ['', '']



expo install react-native-gesture-handler react-native-reanima

npm install react-navigation-drawer

npm install react-navigation-stack

npm install formik
npm install yup













    ############################INVIGILATION START HERE##########

def WebcamInvigilation(request):

    import cv2
    import numpy as np
    import matplotlib.pyplot as plt
    from skimage import img_as_float,img_as_ubyte
    import dlib
    import os

    

    #full screen Mode
    cv2.namedWindow("Smart Invigilation System", cv2.WINDOW_NORMAL)

    #hii ya chini ni kwa screen nzima
    cv2.setWindowProperty("Smart Invigilation System", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

    #ila ukitaka kuweka size mwenyewe tumia hii ya chini
    cv2.resizeWindow("Smart Invigilation System", 1400, 800)

    #Mwisho wa full screen Model








    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    detector = dlib.get_frontal_face_detector()
    predector = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

    def add_photo(img,pt2,mask):
        mask=img_as_float(mask)
        img=img_as_float(img)
        pt1=np.float32([[0,0],
                      [mask.shape[1],0],
                      [0,mask.shape[0]],
                      [mask.shape[1],mask.shape[0]]
                      ])
        mat = cv2.getPerspectiveTransform(pt1,pt2)
        res=cv2.warpPerspective(mask,mat,(img.shape[1],img.shape[0]),cv2.INTER_LINEAR,cv2.BORDER_CONSTANT,borderValue=(-1, -1, -1))

        return res

    def pro(img,mask,draw_rect1=True,draw_rect2=True,draw_lines=True,draw_mask=True):
        copy = img.copy()
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        faces=detector(gray, 0)

        for face in faces:
            x1 = face.left()
            y1 =face.top()
            x2= face.right()
            y2= face.bottom()
            landmarks = predector(gray,face)

            size = copy.shape
            #2D image points. If you change the image, you need to change vector
            image_points = np.array([
                                    (landmarks.part(33).x,landmarks.part(33).y),     # Nose tip
                                    (landmarks.part(8).x,landmarks.part(8).y),       # Chin
                                    (landmarks.part(36).x,landmarks.part(36).y),     # Left eye left corner
                                    (landmarks.part(45).x,landmarks.part(45).y),     # Right eye right corne
                                    (landmarks.part(48).x,landmarks.part(48).y),     # Left Mouth corner
                                    (landmarks.part(54).x,landmarks.part(54).y)      # Right mouth corner
                                ], dtype="double")

            # 3D model points.
            model_points = np.array([
                                    (0.0, 0.0, 0.0),             # Nose tip
                                    (0.0, -330.0, -65.0),        # Chin
                                    (-225.0, 170.0, -135.0),     # Left eye left corner
                                    (225.0, 170.0, -135.0),      # Right eye right corne
                                    (-150.0, -150.0, -125.0),    # Left Mouth corner
                                    (150.0, -150.0, -125.0)      # Right mouth corner

                                ])
            # Camera internals
            focal_length = size[1]
            center = (size[1]/2, size[0]/2)
            camera_matrix = np.array(
                                [[focal_length, 0, center[0]],
                                [0, focal_length, center[1]],
                                [0, 0, 1]], dtype = "double"
                                )

            dist_coeffs = np.zeros((4,1)) # Assuming no lens distortion
            (success, rotation_vector, translation_vector) = cv2.solvePnP(model_points, image_points, camera_matrix, dist_coeffs)

            (b1, jacobian) = cv2.projectPoints(np.array([(350.0, 270.0, 0.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b2, jacobian) = cv2.projectPoints(np.array([(-350.0, -270.0, 0.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b3, jacobian) = cv2.projectPoints(np.array([(-350.0, 270, 0.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b4, jacobian) = cv2.projectPoints(np.array([(350.0, -270.0, 0.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

            (b11, jacobian) = cv2.projectPoints(np.array([(450.0, 350.0, 400.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b12, jacobian) = cv2.projectPoints(np.array([(-450.0, -350.0, 400.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b13, jacobian) = cv2.projectPoints(np.array([(-450.0, 350, 400.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)
            (b14, jacobian) = cv2.projectPoints(np.array([(450.0, -350.0, 400.0)]), rotation_vector, translation_vector, camera_matrix, dist_coeffs)

            b1 = ( int(b1[0][0][0]), int(b1[0][0][1]))
            b2 = ( int(b2[0][0][0]), int(b2[0][0][1]))
            b3 = ( int(b3[0][0][0]), int(b3[0][0][1]))
            b4 = ( int(b4[0][0][0]), int(b4[0][0][1]))

            b11 = ( int(b11[0][0][0]), int(b11[0][0][1]))
            b12 = ( int(b12[0][0][0]), int(b12[0][0][1]))
            b13 = ( int(b13[0][0][0]), int(b13[0][0][1]))
            b14 = ( int(b14[0][0][0]), int(b14[0][0][1]))

            if draw_rect1 ==True:
                cv2.line(copy,b1,b3,(255,255,0),10)
                cv2.line(copy,b3,b2,(255,255,0),10)
                cv2.line(copy,b2,b4,(255,255,0),10)
                cv2.line(copy,b4,b1,(255,255,0),10)

            if draw_rect2 ==True:
                cv2.line(copy,b11,b13,(255,255,0),10)
                cv2.line(copy,b13,b12,(255,255,0),10)
                cv2.line(copy,b12,b14,(255,255,0),10)
                cv2.line(copy,b14,b11,(255,255,0),10)

            if draw_lines == True:
                cv2.line(copy,b11,b1,(0,255,0),10)
                cv2.line(copy,b13,b3,(0,255,0),10)
                cv2.line(copy,b12,b2,(0,255,0),10)
                cv2.line(copy,b14,b4,(0,255,0),10)

            if draw_mask ==True:
                pt=np.float32([b11,b13,b14,b12])

                ty=add_photo(copy,pt,mask)
                tb= img_as_ubyte(ty)

                for i in range(0,ty.shape[0]):
                    for j in range(0,ty.shape[1]):
                        k=ty[i,j]
                        if k[0] != -1 and k[1] != -1 and k[2] != -1:
                            copy[i,j] = tb[i,j]

        return copy

    #change the photo
    mask=cv2.imread("cheating.png")

    # the video
    cap = cv2.VideoCapture(0)

    if (cap.isOpened() == False):
        print("Unable to read camera feed")

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))

    out = cv2.VideoWriter('output.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))

    while(True):
        ret, frame = cap.read()

        if ret == True:
            res=pro(frame,mask,draw_mask=True)
            cv2.imshow('head',res)
            # Write the frame into the file 'output.avi'
            out.write(res)

            # Break the loop
        else:
            break
        key = cv2.waitKey(10)
        # Escキーが押されたら
        if key == 27:
            cv2.destroyAllWindows()
            break

    # When everything done, release the video capture and video write objects
    cap.release()
    out.release()
    return redirect('homePage')