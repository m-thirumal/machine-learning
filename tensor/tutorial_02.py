import tensorflow as tf

# Placeholder
x = tf.placeholder(tf.int64, shape=[3], name='x')
y = tf.placeholder(tf.int64, shape=[3], name='y')

sum_x = tf.reduce_sum(x, name="sum_x")
print("Sum x: ", sum_x)
prod_y = tf.reduce_prod(y, name="prod_y")
print("Prod y: ", prod_y)

div = tf.div(sum_x, prod_y, name='div')

mean = tf.reduce_mean([sum_x, prod_y], name='mean')
session = tf.Session()

print("Sum (x)", session.run(sum_x, feed _dict={x: [100, 200, 300]}))
print("prod y: ", session.run(prod_y, feed_dict={y: [1, 2, 3]}))

writer = tf.summary.FileWriter('./tutorial_02', session.graph)
writer.close()
session.close()
exit()