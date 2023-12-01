import day12


def test_arrangements_2():
    assert day12.count_arrangements_2('???.### 1,1,3') == (1, 1)
    assert day12.count_arrangements_2('.??..??...?##. 1,1,3') == (4, 16384)
    assert day12.count_arrangements_2('?#?#?#?#?#?#?#? 1,3,1,6 ') == (1, 1)
    assert day12.count_arrangements_2('????.#...#... 4,1,1') == (1, 16)
    assert day12.count_arrangements_2('????.######..#####. 1,6,5') == (4, 2500)
    assert day12.count_arrangements_2('?###???????? 3,2,1') == (10, 506250)
