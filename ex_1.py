import tensorflow as tf
print(tf.version)
print("_"*100)

string = tf.Variable("is a string", tf.string)
number = tf.Variable(369, tf.int16)
floating = tf.Variable(6.414, tf.float32)
print(string, "\n", number, "\n", floating)
print("_"*100)

rank1_tensor = tf.Variable(["test"], tf.string)
rank2_tensor = tf.Variable(["test1", "test2"], ["test3", "test4"], tf.string)
print(tf.rank(rank1_tensor))
print(tf.rank(rank2_tensor))
print("_"*100)

shape1 = rank1_tensor.shape
shape2 = rank2_tensor.shape
print(shape1)
print(shape2)
print("_"*100)

tensor1 = tf.ones([1,2,3])
print(tensor1)
tensor2 = tf.reshape(tensor1, [2,3,1])
print(tensor2)
tensor3 = tf.reshape(tensor2,[3, -1])
print(tensor3)
print("_"*100)

t = tf.zeros([5,5,5,5])
print(t)
e = tf.reshape(t, [625])
print(e)