class Players:
    def __init__(self, inputNama, inputNegara, inputClub):
        self.nama = inputNama
        self.negara = inputNegara
        self.club = inputClub

Football1 = Players("Lionel_Messi","Argentina","Paris_saint_germain")
Football2 = Players("Cristiano_Ronaldo","Portugal","Manchester_United")

print(Football1.__dict__)