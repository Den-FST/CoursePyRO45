from ex1 import Person

def test_person():

    p = Person("Ion", 30, 1.75, 75)
    assert p.get_name() == "Ion"
    assert p.get_age() == 30
    assert p.get_height() == 1.75
    assert p.get_weight() == 75

    p.set_name("Ioana")
    assert p.get_name() == "Ioana"
    p.set_age(35)
    assert p.get_age() == 35
    p.set_height(1.80)
    assert p.get_height() == 1.80
    p.set_weight(80)
    assert p.get_weight() == 80


    assert p.bmi() == 0.2469135802

    p2 = Person("Andrea", 25, 1.65, 60)
    p3 = Person("Max", 40, 1.80, 90)
    assert p2.get_name() == "Andrea"
    assert p3.get_name() == "Max"

