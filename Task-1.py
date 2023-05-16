import cv2
import numpy as np
image_data =np.zeros((1024,1024,3), np.uint8)

cv2.rectangle(image_data,(100,412),(300,612),(165,156,69),-1)
cv2.rectangle(image_data,(308,412),(508,612),(54,83,218),-1)
cv2.rectangle(image_data,(516,412),(716,612),(56,146,240),-1)
cv2.rectangle(image_data,(724,412),(924,612),(235,130,57),-1)
cv2.rectangle(image_data,(308,204),(508,404),(185,66,104),-1)
cv2.rectangle(image_data,(308,620),(508,820),(106,46,194),-1)

cv2.circle(image_data,(200,512),20,(226,239,255),-1)

cv2.circle(image_data,(764,572),20,(226,239,255),-1)
cv2.circle(image_data,(881,452),20,(226,239,255),-1)

cv2.circle(image_data,(408,304),20,(226,239,255),-1)
cv2.circle(image_data,(348,364),20,(226,239,255),-1)
cv2.circle(image_data,(468,244),20,(226,239,255),-1)

cv2.circle(image_data,(348,780),20,(226,239,255),-1)
cv2.circle(image_data,(468,660),20,(226,239,255),-1)
cv2.circle(image_data,(348,660),20,(226,239,255),-1)
cv2.circle(image_data,(468,780),20,(226,239,255),-1)

cv2.circle(image_data,(408,512),20,(226,239,255),-1)
cv2.circle(image_data,(348,572),20,(226,239,255),-1)
cv2.circle(image_data,(468,452),20,(226,239,255),-1)
cv2.circle(image_data,(348,452),20,(226,239,255),-1)
cv2.circle(image_data,(468,572),20,(226,239,255),-1)

cv2.circle(image_data,(556,572),20,(226,239,255),-1)
cv2.circle(image_data,(616,572),20,(226,239,255),-1)
cv2.circle(image_data,(676,452),20,(226,239,255),-1)
cv2.circle(image_data,(556,452),20,(226,239,255),-1)
cv2.circle(image_data,(616,452),20,(226,239,255),-1)
cv2.circle(image_data,(676,572),20,(226,239,255),-1)

cv2.putText(image_data,"Yash Agrawal",(600,700),cv2.FONT_HERSHEY_COMPLEX_SMALL ,2,(255,255,255),2)
cv2.putText(image_data,"122EI0173",(600,750),cv2.FONT_HERSHEY_COMPLEX_SMALL ,2,(255,255,255),2)
cv2.putText(image_data,cv2. __version__ ,(600,800),cv2.FONT_HERSHEY_COMPLEX_SMALL ,2,(255,255,255),2)

cv2.imshow('Ravi',image_data)
cv2.imwrite('Task-1.jpg',image_data)
cv2.waitKey(0)
cv2.destroyAllWindows()
