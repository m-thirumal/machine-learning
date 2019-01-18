import tensorflow as tf

#variable
#Y = MX + C
m = tf.Variable([2.5, 4.0], name='Var_m')
x = tf.placeholder(tf.float32, name='x')
c = tf.Variable([5.0, 10.0], name='Var_c')

y = m * x + c

# Initailize the vaiable
init = tf.global_variables_initializer()

with tf.name_scope("Equation_y"):
    with tf.Session() as session:
        session.run(init)
        print("Final result Y = ", session.run(y, feed_dict={x:[10, 100]}))

# s  = mx
s = m * x

# Initialize only those variables that you might need
init = tf.variables_initializer([m])
with tf.name_scope("Equation_S"):
    with tf.Session() as session:
        session.run(init)
        print("Will work ? mx + c: ", session.run(s, feed_dict={x:[10, 100]}))

number = tf.Variable(2)
multiplier = tf.Variable(1)
init = tf.global_variables_initializer()
result = number.assign(tf.multiply(number, multiplier))

with tf.Session() as session:
    session.run(init)
    for i in range(10):
        print("Result number * multipler: ", session.run(result))
        print("Increment multipler: ", session.run(multiplier.assign_add(1)))

# Tensor board
writer = tf.summary.FileWriter('./tutorial_04', session.graph)
writer.close()
session.close()
exit()