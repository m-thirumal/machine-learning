import tensorflow as tf

# y = mx + c
# Constant
m = tf.constant([10, 200], name='m')
# Placeholder
x = tf.placeholder(tf.int32, name='x')
b = tf.placeholder(tf.int32, name='b')
# MX
mx = tf.multiply(m, x, name='mx')
# Y
y = tf.add(mx, b, name='y')
# y
y_ = tf.subtract(mx, b, name='y_')
# Session
with tf.Session() as session:
    print("MX: ", session.run(mx, feed_dict={x:[12, 2]}))
    print("Y: ", session.run(y, feed_dict={x:[2, 2,], b:[1, 4]}))
    print("Y_ :, ", session.run(fetches=[y, y_], feed_dict={x:[2, 3], b:[4, 5]}))
#tensor board
writer = tf.summary.FileWriter('./tutorial_03', session.graph)
writer.close()
session.close()
exit()
