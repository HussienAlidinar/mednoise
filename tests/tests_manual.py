from mednoise import manual as md

md.manual_merge("tests/images/*", (0,0,0), (255, 0, 0))

restraints = [(473,91),(214,601),(764,626)]

md.manual_edit("tests/images/*", xy = restraints)

md.manual_primer("tests/images/*") 
