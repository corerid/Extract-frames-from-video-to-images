import cv2

step = 10
start_frame = 0

def FrameCapture(path):
    vidObj = cv2.VideoCapture(path)

    # fps = vidObj.get(cv2.CAP_PROP_FPS)
    # print ('FPS : ', fps)

    total_frame = vidObj.get(7)
    print ('Total frame : ',total_frame)
    frame_no = start_frame
    count = 0
    success = 1

    while success:
        vidObj.set(1,frame_no);
        success, image = vidObj.read()
        cv2.imwrite("tmp_dataset/img%d.jpg" % count, image)
        frame_no += step
        count += 1

    #print (count)

if __name__ == '__main__':
    #Video file name
    FrameCapture("drone9.mkv")
