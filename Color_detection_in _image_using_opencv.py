import cv2
import pandas as pd

img_path = 'C:/Users/Mohit Mukamia/Desktop/color_detection using opencv/image_color.jpg'
csv_path = 'C:/Users/Mohit Mukamia/Desktop/color_detection using opencv/colors.csv'

# read csv file
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(csv_path, names=index, header=None)

# read image
img = cv2.imread(img_path)
img = cv2.resize(img, (800,600))

# declare global variables
clicked = False
r = g = b = xpos = ypos = 0

# function to get the min distance from all colors and get the nearest matching color
def get_color_name(R,G,B):
	minimum = 1000
	for i in range(len(df)):
		d = abs(R - int(df.loc[i, 'R'])) + abs(G - int(df.loc[i, 'G'])) + abs(B - int(df.loc[i, 'B']))
		if d <= minimum:
			minimum = d
			cname = df.loc[i, 'color_name']
	return cname


# function to get coordinates of cursor
def draw_function(event, x, y, flags, params):
	if event == cv2.EVENT_LBUTTONDBLCLK:
		global b, g, r, xpos, ypos, clicked
		clicked = True
		xpos = x
		ypos = y
		b, g, r = img[y,x]
		b = int(b)
		g = int(g)
		r = int(r)

# creating window to display color
cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_function)

while True:
	cv2.imshow('image', img)
	if clicked:
		cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)
		text = get_color_name(r, g, b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)
		cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

		# For very light colours we will display text in black colour
		if r+g+b >= 600:
			cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

	if cv2.waitKey(20) & 0xFF == 27:
		break

cv2.destroyAllWindows()
