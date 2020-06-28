class Song(object):

    def __init__(self, lytics):
        self.lyrics = lytics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockers full of shells"])

the_yellow_skirt = Song(["淡黄的长裙，蓬松的头发",
                         "牵着我的手，看新展出的油画",
                         "无人的街道，空荡的家里",
                         "就剩我一个人开狂欢的party"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
the_yellow_skirt.sing_me_a_song()