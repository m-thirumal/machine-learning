import tensorflow as tf

# Custom graph

g1 = tf.Graph()

with g1.as_default():
    with tf.Session() as session:
        # Y = mx + c
        m = tf.constant([5, 7], name='const_a')
        x = tf.placeholder(tf.int32, name='x')
        c = tf.constant([3, 4], tf.int32, name='c')
        y = m * x + c
        print("Y: ", session.run(y, feed_dict={x:[10, 100]}))
        assert y.graph is g1


g2 = tf.Graph()

with g2.as_default():
    with tf.Session() as session:
        # Y = m^x
        m = tf.constant([5, 7], name='const_a')
        x = tf.placeholder(tf.int32, name='x')
       # c = tf.constant([3, 4], tf.int32, name='c')
        y = tf.pow(m, x, name='y')
        print("Y: ", session.run(y, feed_dict={x:[20, 200]}))
        assert y.graph is g2



#tensor board
writer = tf.summary.FileWriter('./tutorial_05', session.graph)
writer.close()
session.close()
exit()
