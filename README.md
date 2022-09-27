# diabeticRetinopathy
Application of Deep Learning in Retinal Imaging
Detected Diabetic Retinopathy (DR) using Deep Learning techniques on the EyePACS dataset
Model trained on fundus images of patients with diabetes to detect DR, and graded them as non-DR,
mild Non-Proliferative DR (NPDR), moderate NPDR, severe NPDR or Proliferative DR
The model architecture involved Convoluted Neural Networks (CNNs)
Gained sufficient exposure working with TensorFlow, Keras, InceptionV3, and Medical Image Processing.

I tried different CNN Architectures and different optimizers for getting the highest possible accuracy.
1)First I tried on a simple 3 layered Architecture which I built myself, and got a baseline accuracy score.
2)Then I used VGG16 model architecture which gave accuracy score in comparison with the above model, which was not expected. I expected a better accuracy from VGG16 model.
3)I then used hyperparameter tuning using Keras tuner, tried different number of filters in each layer, different sizes of kernel, and different learning rates of adam optimizer. The best model was clearly overfitting the training data after 25 epochs, as train accuracy reached over 0.99, while validation accuracy declined to below 0.70. I will use regularization techniques to avoid overfitting.
4)Then I used the InceptionV3 model architecture, pretrained over the ImageNet dataset. This model used RMSProp optimizer with learning rate as 0.001.



