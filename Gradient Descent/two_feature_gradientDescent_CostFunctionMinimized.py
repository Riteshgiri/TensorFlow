Python 3.5.2 (v3.5.2:4def2a2901a5, Jun 25 2016, 22:18:55) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import tensorflow as tf

>>> theta0=tf.Variable(0.3,tf.float32)
>>> theta1=tf.Variable(-0.3,tf.float32)
>>> theta2=tf.Variable(0.3,tf.float32)
>>> x=tf.placeholder(tf.float32)
>>> y=tf.placeholder(tf.float32)
>>> z=tf.placeholder(tf.float32)
>>> h=theta0+(theta1*x)+(theta2*z)
>>> J=tf.reduce_sum(tf.square(h-y))
>>> sess=tf.Session()
>>> init=global_variables_initializer()
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    init=global_variables_initializer()
NameError: name 'global_variables_initializer' is not defined
>>> init=global_variables_initializer()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    init=global_variables_initializer()
NameError: name 'global_variables_initializer' is not defined
>>> init=tf.global_variables_initializer()
>>> sess.run(init)
>>> for i in range(1000):
	sess.run()

	
Traceback (most recent call last):
  File "<pyshell#16>", line 2, in <module>
    sess.run()
TypeError: run() missing 1 required positional argument: 'fetches'
>>> optimizer=tf.train.GradientDescentOptimizer(0.01)
>>> train=optimizer.minimize(J)
>>> for i in range(1000)
SyntaxError: invalid syntax
>>> for i in range(1000):
	sess.run(train,{x:[1,2,3,4],y:[0,-1,-2,-3],z:[2,3,4,5]})

	
>>> print(sess.run([theta0,theta1,theta2]))
[0.89999819, -1.0999985, 0.099999346]
>>> #the above values of theta0,theta1,theta2 minimize the cost function and thus helps us in finding the perfect line that could fit the given dataset.
>>> 
