import sys

def setup(core, object):
	object.setAttachment('radial_filename', 'deeds/structureDeed')
	object.setConstructorTemplate('object/building/player/construction/shared_construction_player_house_generic_medium_style_02.iff')
	object.setStructureTemplate('object/tangible/deed/player_house_deed/shared_generic_house_medium_windowed_s02_deed.iff')
	object.setLotRequirement(2)
	object.setBMR(18)
	return

def use(core, actor, object):
	return