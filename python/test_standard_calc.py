from standard_calc import bound_to_180, is_angle_between


""" Tests for bound_to_180() """


def test_bound_basic1():
    # edge cases
    assert bound_to_180(0) == 0
    assert bound_to_180(180) == -180
    assert bound_to_180(-180) == -180
    assert bound_to_180(360) == 0
    assert bound_to_180(-360) == 0
    assert bound_to_180(720) == 0
    assert bound_to_180(-720) == 0
    # normal cases
    assert bound_to_180(135) == 135
    assert bound_to_180(200) == -160
    assert bound_to_180(-190) == 170
    assert bound_to_180(540) == -180
    assert bound_to_180(-540) == -180

""" Tests for is_angle_between() """


def test_between_basic1():
    assert is_angle_between(0, 1, 2)
    assert not is_angle_between(0, 359, 1)
    assert is_angle_between(350, 10, 20)
    assert not is_angle_between(350, 340, 10)
    assert is_angle_between(-10, 0, 10)
    assert not is_angle_between(-10, -20, 10)
    assert is_angle_between(170, -170, -160)
