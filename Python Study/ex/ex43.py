from sys import exit
from random import randint
from textwrap import dedent  # 它会把三引号字符串开头的空白去掉，不然排版就会很失败

# 场景


class Scene(object):

    def enter(self):
        print("此场景尚未配置.")
        print("加油，奥利给！")
        exit(1)

# 引擎


class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        # 打开当前场景
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

# 死亡场景


class Death(Scene):
    quips = [
        "你死了，死的很恶心。",
        "你妈妈会很自豪的...因为你光荣了。",
        "Such a luser.",
        "我家的狗都比你会玩。",
        "你比山姆叔叔的苹果派还糟糕。"
    ]

    def enter(self):
        # 随机来一句俏皮话
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

# 中央走廊
class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""                 
            来自Percal 25号行星的哥顿人入侵了你的飞船，湮灭了你的全体船员。
            你是最后的希望。
            你的最后一个任务是从武器库中取出强磁挥拳加速重氢装置，把它放在舰桥上，在进入逃生舱后炸毁飞船。
            心有万千沟壑，眼有如炬火光
            奔涌吧，后浪！


            你正沿着中央走廊跑去拿武器
            军械库中突然一个哥顿人跳出来，
            红色的鳞状皮肤，黑色肮脏的牙齿，邪恶的小丑服装在他充满仇恨的身体上流淌。
            他堵住了军械库的门，正要拔出光剑陪你玩Beat Saber。
        """))
        action = input('>')
        if action == "shoot!":
            print(dedent("""
            
            
            
            """))

# 激光武器库
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

# 主控仓


class TheBridge(Scene):

    def enter(self):
        pass

# 救生舱


class EscapePod(Scene):

    def enter(self):
        pass

# 地图


class Map(object):
    def __init__(self, start_scene):
        pass

    def next_scene(self, scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
