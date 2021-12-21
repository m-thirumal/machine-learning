import tensorflow as tf

# Declare & assign constant
a = tf.constant(6, name='constant_a')
b = tf.constant(3, name='constant_b')
c = tf.constant(10, name='constant_c')
d = tf.constant(5, name='constant_d')

# Operation
mul = tf.multiply(a, b, name='Mul')
print('Multiply: ', mul)
div = tf.divide(c, d, name='div')
print('Division: ', div)
addn = tf.add_n([mul, tf.cast(div, tf.int32)], name='addn')

print("Addition: ", addn)

session = tf.Session()

print("Add output: ", session.run(addn))

# Tensor board

writer = tf.summary.FileWriter('./tutorial_01', session.graph)
writer.close()
session.close()
exit()