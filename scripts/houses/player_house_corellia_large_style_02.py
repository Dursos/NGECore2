import sys
from services.housing import HouseTemplate
from engine.resources.scene import Point3D

def setup(core):
	houseTemplate = HouseTemplate("object/tangible/deed/player_house_deed/shared_corellia_house_large_style_02_deed.iff", "object/building/player/shared_player_house_generic_large_style_02.iff", 2)
	
	houseTemplate.addBuildingSign("object/tangible/sign/player/shared_house_address.iff", Point3D(1, 2, 3))
	houseTemplate.addPlaceablePlanet("corellia")
	houseTemplate.addPlaceablePlanet("talus")
	houseTemplate.setDefaultItemLimit(500)
	
	core.housingService.addHousingTemplate(houseTemplate)
	return