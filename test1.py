import tensorflow as tf
a=tf.constant(2)
b=tf.constant(3)
c=tf.constant(4)
x=tf.add(a,b)
y=tf.add(x,c)
with tf.Session() as s:
	writer=tf.summary.FileWriter('.\\graphs',s.graph)
	print(s.run(y))

writer.close()