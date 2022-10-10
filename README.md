# diabeticRetinopathy
Application of Deep Learning in Retinal Imaging
Detected Diabetic Retinopathy (DR) using Deep Learning techniques on the EyePACS dataset
Model trained on fundus images of patients with diabetes to detect DR, and graded them as non-DR,
mild Non-Proliferative DR (NPDR), moderate NPDR, severe NPDR or Proliferative DR
The model architecture involved Convoluted Neural Networks (CNNs)
Gained sufficient exposure working with TensorFlow, Keras, InceptionV3, and Medical Image Processing.
The dataset used for this research purpose is the EYEPACS Dataset."https://www.kaggle.com/competitions/diabetic-retinopathy-detection/data" 
It is derived from the original paper "https://www.nature.com/articles/s41467-021-23458-5#MOESM1".
This dataset contains about 35000 fundus images, while the original paper's model was trained on about 466,000 images, and tested on about 200,000 images.

I tried different CNN Architectures and different optimizers for getting the highest possible accuracy.
1)First I tried on a simple 3 layered Architecture which I built myself, and got a baseline accuracy score.
2)Then I used VGG16 model architecture which gave accuracy score in comparison with the above model, which was not expected. I expected a better accuracy from VGG16 model.
3)I then used hyperparameter tuning using Keras tuner, tried different number of filters in each layer, different sizes of kernel, and different learning rates of adam optimizer. The best model was clearly overfitting the training data after 25 epochs, as train accuracy reached over 0.99, while validation accuracy declined to below 0.70. I will use regularization techniques to avoid overfitting.
4)Then I used the InceptionV3 model architecture, pretrained over the ImageNet dataset. This model used RMSProp optimizer with learning rate as 0.001.

A major issue which I noticed with the different models I used was that both the accuracy and val_accuracy would remain around the same range of 73%. Even after 20 epochs the accuracy would not change at all. It wont fluctuate but it wont increase either. So, I tried using different techniques to cure for the same. I tried reducing the learning rate, which did not help. Then I tried to reduce the complexity of the model along with using regularizers, which again did not help a lot. The accuracy would still remain constant at the same level even though it increased a bit. I also tried correcting for class imbalance in the dataset by assigining class weights. The distribution of images was as follows: {0:6150,1:588,2:1283,3:221,4:166}. After using scikit-learn class_weight the weight distribution was: 
{0: 0.2734959349593496,
 1: 2.856900212314225,
 2: 1.310223953261928,
 3: 7.6022598870056495,
 4: 10.117293233082707}
The result was slightly improved to 0.7394 accuracy and 0.7356 val_accuracy.

Then I used Transfer learning techniques and used the VGG16 model trained on ImageNet dataset. This gave the best validation accuracy in comparison to all the previous literatures available on this particular dataset. This model gave an accuracy of 0.75 on training set and an accuracy 1.00 on testing dataset. It had an auc of 0.9014 on training set and an auc of 1.00 on testing set.


