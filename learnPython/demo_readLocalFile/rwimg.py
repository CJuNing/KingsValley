fs1 = open('input/1.png', 'r')
fs2 = open('output/1.png', 'w+')
fs2.write(fs1.read())
fs1.close()
