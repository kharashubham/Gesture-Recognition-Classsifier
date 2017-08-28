# Gesture-Recognition-Classsifier
A highly accurate(98%) SVM classifier to recognise gestures performed using a mobile phone (or any other device which may use 
an accelerometer)

This project is a staright forward implementation of the following paper : 
https://stanford.edu/~sxie/Michael%20Xie,%20David%20Pan,%20Accelerometer%20Gesture%20Recognition.pdf

We were able to replicate the results in papers using the popular libraries directly like Numpy and Sklearn.

<b>DATA :</b> <br>

The data we used was collected using an iPhone, for someone who hasn't read the paper : the data is basically accelerometer data 
collected in 2 second window when the gesture action was performed. We needed 100 data points for each of the x,y & z axis but
there were inconsistencies in recording the data neatly in one go and in the desired amount. So after a little bit of hard coding 
and linear interpolation we had our data to be used by the algorithm ready. We used this data to replicate the results in paper,
which are fairly good.

So this data for 4 gestures is in good form to be used as is on any algorithm/model that may require similar type of data.

Anyone trying to implement this paper from scratch and is not able to replicate the results please feel free to get in touch, We would
love to contribute.
