import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'deeds/harvesterDeed')
	object.setConstructorTemplate('object/installation/mining_ore/construction/shared_construction_mining_ore_harvester_style_heavy.iff')
	object.setStructureTemplate('object/installation/mining_liquid/shared_mining_liquid_harvester_style_3.iff')
	object.setLotRequirement(1)
	object.setBMR(90)
	return