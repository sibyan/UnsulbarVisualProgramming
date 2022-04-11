class Football():
    def __init__(self, nama, negara, club):
        self.nama = nama
        self.negara = negara
        self.club = club

    def cek_id_football(self):
        print('nama:',self.nama, '\negara:',self.negara, '\club:',self.club)

class Ball(Football):
    def cek_id_football(self):
        print('cek aja ball appsnya')

toko1 = Football('Lionel_Messi','Argentina', 'Paris_Saint_Germain')
toko2 = Football('Cristiano_Ronaldo','Portugal', 'Manchester_United')

toko1.cek_id_football
toko2.cek_id_footballss