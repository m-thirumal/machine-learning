import tensorflow as tf

# name scope for tensor board

A = tf.constant([4], tf.int32, name='A')
B = tf.constant([5], tf.int32, name='B')
C = tf.constant([6], tf.int32, name='C')

x = tf.placeholder(tf.int32, name='x')

# y = Ax^2 + Bx + C

with tf.name_scope("Equation_1"):
    Ax2 = tf.multiply(A, tf.pow(x, 2, name='x2'), name='AX2')
    Bx = tf.multiply(B, x, name='BX')
    y1 = tf.add_n([Ax2, Bx, C], name='Y1')

# y = AX^2 + Bx^2
with tf.name_scope("Equation_2"):
    Ax2 = tf.multiply(A, tf.pow(x, 2, name='x2'), name='AX2')
    Bx2 = tf.multiply(B, tf.pow(x, 2, name='x2'), name='BX2')
    y2 = tf.add_n([Ax2, Bx2, C], name='Y2')

# y = y1 + y2
with tf.name_scope("Equation_Y"):
    y = tf.add(y1, y2, name='Y')

with tf.Session() as session:
    print(" Y: ", session.run(y, feed_dict={x:[10]}))

# Tensor board
writer = tf.summary.FileWriter('./tutorial_06', session.graph)
writer.close()
session.close()
exit()