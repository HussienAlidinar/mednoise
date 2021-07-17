from mednoise import hotspot as md

md.hotspot_complete("tests/images/*", 50, 50)

md.hotspot_calculator("tests/images/EXAMPLE_MEDNOISE_1.PNG", 50, 50)

md.hotspot_analyzer(calc = storeddictionary, filepath = "tests/images/EXAMPLE_MEDNOISE_1.PNG", x = 50, y = 50)

md.hotspot_isolator(calc = analyzedval, filepath = "tests/images/EXAMPLE_MEDNOISE_1.PNG", x = 50, y = 50)
