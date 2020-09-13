import utili
import cv2

input_video=r'C:\Users\User\Desktop\Simple motion detection\Traffic-27260.mp4'

    
video = cv2.VideoCapture(input_video)
bg = cv2.createBackgroundSubtractorMOG2(history=1000, varThreshold=100, detectShadows=False)
    
while (1):
        
    et, frame = video.read()
  
    fg = bg.apply(frame)
    
    closing= utili.video_preprocessing(fg)
        
    rect=utili.finding_contours(closing,80,80,frame)
    
    utili.create_rect(rect,frame)
    
    
    
    # cv2.imshow('foreground',fg)
    # cv2.imshow('dilation',dilation)
    cv2.imshow('original',frame)
        
  
    if cv2.waitKey(1)  == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
    
