from main import Game
from main import PacmanMap
from main import Pacman, Player
import pytest
from copy import copy

def test_x():
    assert PacmanMap() is not None

def test_adding_object_to_map():
    pmap = PacmanMap()
    pmap.add_object(1, 1, None)

    assert pmap.get_object(1, 1) is None

def test_adding_object_to_map_second():
    pmap = PacmanMap()
    pmap.add_object(0, 0, 1)
    with pytest.raises(IndexError):
        pmap.add_object(31, 20, 1)
        pmap.add_object(32, 0, 1)
        assert pmap.get_object(31, 20) == 1
        assert pmap.get_object(32, 0) == 1

    assert pmap.get_object(0, 0) == 1

def test_get_map_element_when_empty():
    pmap = PacmanMap()
    assert pmap.get_object(0,0) == None

def test_map_has_boundries():
    pmap = PacmanMap()
    pmap.lets_build_a_wall()
    for x in range(pmap.MAX_X):
        assert pmap.get_object(x, 0) == 0
    for x in range(pmap.MAX_X):
        assert pmap.get_object(0, x) == 0
    for y in range(pmap.MAX_Y):
        assert pmap.get_object(y, 0) == 0
    for y in range(pmap.MAX_Y):
        assert pmap.get_object(0, y) == 0




def test_pacman_on_starting_positon():
    pmap = PacmanMap()
    hero = Pacman()
    assert hero.get_position() == (15, 15)

def test_pacman_is_alive_on_start():
    pmap = PacmanMap()
    hero = Pacman()
    assert hero.get_life_points()

def test_start_direction_pacman():
    hero = Pacman()
    assert hero.movement_direction is None

def test_change_direction():
    hero = Pacman()
    hero.set_direction(Pacman.LEFT) 
    assert hero.movement_direction == Pacman.LEFT

def test_change_wrong_direction():
    hero = Pacman()
    with pytest.raises(ValueError):
        hero.set_direction(-1)

def test_move_player_without_direction():
    hero = Player()
    start_position = hero.get_position()
    hero.move()
    assert hero.get_position() == start_position

def test_move_player_left():
    hero = Player()
    hero.position = [1, 1]
    start_position = copy(hero.get_position())
    hero.set_direction(Player.LEFT)
    hero.move()
    start_position[0] -= 1
    assert hero.get_position() == start_position

def test_move_player_right():
    hero = Player()
    hero.position = [1, 1]
    start_position = copy(hero.get_position())
    hero.set_direction(Player.RIGHT)
    hero.move()
    start_position[0] += 1
    assert hero.get_position() == start_position

def test_move_player_up():
    hero = Player()
    hero.position = [1, 1]
    start_position = copy(hero.get_position())
    hero.set_direction(Player.UP)
    hero.move()
    start_position[1] -= 1
    assert hero.get_position() == start_position

def test_move_player_down():
    hero = Player()
    hero.position = [1, 1]
    start_position = copy(hero.get_position())
    hero.set_direction(Player.DOWN)
    hero.move()
    start_position[1] += 1
    assert hero.get_position() == start_position

def test_is_game_initialised():
    game = Game()
    game.init()
    assert game.pacman is not None
    assert game.pmap is not None

def test_is_move_valid_against_wall():
    pass
