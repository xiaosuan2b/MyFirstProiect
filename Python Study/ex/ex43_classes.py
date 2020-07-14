#场景
class Scene(object):

    def enter(self):
        pass

#引擎
class Engine(object):
    def __init__(self,scene_map):
        pass

    def play(self):
        pass

#死亡场景
class Death(Scene):

    def enter(self):
        pass

#中央走廊
class CentralCorridor(Scene):

    def enter(self):
        pass

#激光武器库
class LaserWeaponArmory(Scene):

    def enter(self):
        pass

#主控仓
class TheBridge(Scene):

    def enter(self):
        pass

#救生舱
class EscapePod(Scene):

    def enter(self):
        pass

#地图
class Map(object):
    def __init__(self,start_scene):
        pass
    
    def next_scene(self,scene_name):
        pass

    def opening_scene(self):
        pass


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()