from mednoise import branch as md

md.branch_complete("tests/images/*", 450, 350, iterations = 500)

md.branch_calculator("tests/images/EXAMPLE_MEDNOISE_1.PNG", 450, 350, iterations = 500)

md.branch_analyzer(coords)

md.branch_isolator("tests/images/EXAMPLE_MEDNOISE_1.PNG", g)
