Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf
>>> theta0=tf.Variabla(0.3,tf.float32)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    theta0=tf.Variabla(0.3,tf.float32)
AttributeError: module 'tensorflow' has no attribute 'Variabla'
>>> theta0=tf.Variable(0.3,tf.float32)
>>> theta1=tf.Variable(-0.3,tf.float32)
>>> x-tf.placeholder(tf.float32)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    x-tf.placeholder(tf.float32)
NameError: name 'x' is not defined
>>> x=tf.placeholder(tf.float32)
>>> y=tf.placeholder(tf.float32)
>>> h=theta0+theta1*x
>>> J=tf.reduce_sum(tf.square(h-y))
>>> sess=tf.Session()
>>> init=tf.global_variables_initializer()
>>> sess.run(init)
>>> optimizer=tf.train.GradientDescentOptimizer(0.01)
>>> train=optimizer.minimize(J)
>>> print(sess.run([theta0,theta1]))
[0.30000001, -0.30000001]
>>> #In the above line we dint enter inputs x,y. Thus theta0 & theta1 vales unchanged
>>> for i=1:1000,
SyntaxError: invalid syntax
>>> for i in range(1000):
	sess.run(J,{x:[1,2,3,4],y:[0,-1,-2,-3]})

	
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
6.8599992
>>> for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3]})

	
>>> print(sess.run([theta0,theta1]))
[0.99999493, -0.99999827]
>>> #theta0=0.99999493,theta1=-0.99999827 for the line "h=theta0+theta1*x" to be the perfect line through our dataset of x and y.
>>> #Cost function minimized
>>> 
