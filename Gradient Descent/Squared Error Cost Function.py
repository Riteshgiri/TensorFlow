Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf
>>> theta0=tf.Variable(0.3,tf.float32)
>>> theta1=t.Variable(-0.3,tf.float32)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    theta1=t.Variable(-0.3,tf.float32)
NameError: name 't' is not defined
>>> theta1=tf.Variable(-0.3,tf.float32)
>>> x=tf.placeholder(tf.float32)
>>> h=theta0 + theta1*x
>>> sess=tf.Session()
>>> y=tf.placeholder(tf.float32)
>>> cost_func=tf.reduce_sum(tf.square(h-y))
>>> init=tf.global_variables_initializer()
>>> sess.run(init)
>>> print(sess.run(cost_func,{x:[1,2,3,4],y:[0,-1,-2,-3]}))
6.86
>>> 
