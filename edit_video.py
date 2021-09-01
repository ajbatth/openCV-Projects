import cv2

print("  WELCOME TO VIDEO EDITOR  ".center(80,'#'),end="\n\n")

print("Press 0 to open web camera")
print("Press 1 to connected camera")
print("Press 2 to edit saved video")
Cam=int(input())

if Cam ==2:
    print("Enter the location of video to edit saved video")
    path=input()
    
    cap = cv2.VideoCapture(path)
    
    print("Press \'g\' to convert video into gray-scale")
    print("Press \'n\' for no change")
    color_of_video=input()
    
    print("Press 0 to flip Top-Down")
    print("Press 1 to flip Left-Right")
    print("Press -1 to flip Top-Down & Left-Right")
    print("Press 9 for no change")
    FLIP= int(input())
    
    
    while True:
        ret,frame = cap.read()
        
        if color_of_video=='g':
            frame= cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
            
        if FLIP in (-1,0,1):
            frame=cv2.flip(frame, FLIP)
            
        cv2.imshow('Frame', frame)
        
        
        if cv2.waitKey(25) & 0xFF == ord('q'):   
            break 
    cap.release()
    cv2.destroyAllWindows()

if Cam in (0,1):
    cap = cv2.VideoCapture(Cam, cv2.CAP_DSHOW)
    
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    output = cv2.VideoWriter("output.avi", fourcc, 20.0, (640,480),-1)
    
    print("Press \'g\' to convert video into gray-scale")
    print("Press \'n\' for no change")
    color_of_video=input()
    
    print("Press 0 to flip Top-Down")
    print("Press 1 to flip Left-Right")
    print("Press -1 to flip Top-Down & Left-Right")
    print("Press 9 for no change")
    FLIP= int(input())
    
    while(cap.isOpened()):
        ret,frame = cap.read()
        
        if ret == True:
            if color_of_video == 'g':
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
                
            if FLIP in (-1, 0, 1):
                frame= cv2.flip(frame, FLIP)
            
            output.write(frame)
            
            cv2.imshow("VIDEO", frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break 
cap.release()
output.release()
cv2.destroyAllWindows()           
                 
            
    
        
    
            
            
        

