def biggest_guy(one, two, three):
    # max_number = 0
    # if one > two and one > three:
    #     max_number = one
    #     return max_number
    # elif two > one and two > three:
    #     max_number =  two
    #     return max_number
    # elif three > one and three > two:
    #     max_number = three
    #     return max_number
        
    # if (one >= two) and (one >= three):
    #     max_number = one
    #     return max_number
    # elif (two >= one) and (two >= three):
    #     max_number = two
    #     return max_number

    # else:
    #     max_number = three
    #     return max_number

    # return max_number(max_number(one, two) three)
    return max(one, two, three)
    

def test_biggest_guy():
    try:
        assert biggest_guy(1, 3, 2) == 3
        assert biggest_guy(30, 10, 20) == 30
        assert biggest_guy(20, 10, 30) == 30
        assert biggest_guy(2, 1, 9) == 9
        assert biggest_guy('a', 'a', 'b') == 'b' # 'b' is greater than 'a'
    except (AssertionError) as e:
        print(e)
        print("WRONG!!")
        return None
    print("SUCCESS!!!")
test_biggest_guy()