from api import character


def test_get_character_image_filename():
    assert (
        character.get_character_image_filename(
            "0", "headcircle", "faceneutral", "hairnancy", "hatwinter"
        )
        == "body0headcirclefaceneutralhairnancyhatwinter.png"
    )
