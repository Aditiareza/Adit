from sklearn import tree

bayam = 0
kangkung = 1
kilogram = 0
pcs = 1

tipe = [[150, 1], [180, 1], [300, 0], [350, 0]]
variabel = [0, 0, 1, 1]
reaksi = tree.DecisionTreeClassifier()
reaksi = reaksi.fit(tipe, variabel)

print('Klasifikasi Pesanan Toko Sayuran Segar')
a = input('berapa kilogram ? : ')
b = input('\nPilih Sayuran segar yang anda suka \nBayam atau Kangkung : ')

data = int(a)
if b.lower() == 'kilogram':
    jk = 0
elif b.lower() == 'ikat':
    jk = 1
else:
    print('Terima kasih banyak')

c = reaksi.predict([[data, a]])
if c == 0:
    d = 'bayam'
else:
    d = 'kangkung'

print('Berikut pilihan anda : {}'.format(d))
