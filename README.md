# Object Detection Task

This is a simple object detection task to classify and count the number of apples, oranges, and cats that are present in a given image, although it can be extended to include other objects as well. 

# Approach
I used OpenCV and Tensorflow to load the given image and detect what kinds of objects were present as well as generating the frequency of these distinct objects. I also drew bounding boxes around the different objects using the draw_bbox method from OpenCV. Finally, I used Matplotlib to generate the annotated image and manually constructed a dictionary to store the number of apples, oranges, and cats seen.  

# Steps Taken:
1. Make sure that you have OpenCV and Tensorflow installed on your system. To do so, you can run
```
pip install opencv-python 
```
and 
```
pip install tensorflow 
```
on your terminal to ensure the necessary packages are installed. Assuming your pip is up-to-date, this will also avoid any errors with importing cv2, since this is dependent on whether opencv-python is installed. To update pip to the most current version, run 
```
/Library/Frameworks/Python.framework/Versions/3.9/bin/python3.9 -m pip install --upgrade pip
```

2. Install NumPy and Matplotlib on your system to be able to generate the annotated image. Make sure to run 
```
pip install numpy
```
and 
```
pip install matplotlib
```
on your terminal to do so. 

3. Running the given code will yield an image that roughly looks like this:
![alt text](https://ibb.co/DbPYSFh)
and the dictionary containing the count for cats, apples, and oranges will be displayed on the terminal.
