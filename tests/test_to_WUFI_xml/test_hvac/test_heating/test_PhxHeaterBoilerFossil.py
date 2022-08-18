from PHX.model.hvac import heating, _base, collection
from PHX.to_WUFI_XML.xml_builder import generate_WUFI_XML_from_object
from tests.test_to_WUFI_xml._utils import xml_string_to_list


def test_default_PhxHeaterBoilerFossil(reset_class_counters):
    h1 = heating.PhxHeaterBoilerFossil()
    h1.usage_profile.space_heating = True
    sys = _base.PhxMechanicalSubSystem()
    sys.device = h1
    coll = collection.PhxMechanicalSystemCollection()
    coll.add_new_mech_subsystem(sys.identifier, sys)
    result = generate_WUFI_XML_from_object(coll, _header="")
    assert xml_string_to_list(result) == [
        '<Systems count="1">',
        '<System index="0">',
        '<Name>Ideal Air System</Name>',
        '<Type choice="User defined (ideal system)">1</Type>',
        '<IdentNr>1</IdentNr>',
        '<ZonesCoverage count="1">',
        '<ZoneCoverage index="0">',
        '<IdentNrZone>1.0</IdentNrZone>',
        '<CoverageHeating>1.0</CoverageHeating>',
        '<CoverageCooling>1.0</CoverageCooling>',
        '<CoverageVentilation>1.0</CoverageVentilation>',
        '<CoverageHumidification>1.0</CoverageHumidification>',
        '<CoverageDehumidification>1.0</CoverageDehumidification>',
        '</ZoneCoverage>',
        '</ZonesCoverage>',
        '<Devices count="1">',
        '<Device index="0">',
        '<Name>_unnamed_equipment_</Name>',
        '<IdentNr>1</IdentNr>',
        '<SystemType>3</SystemType>',
        '<TypeDevice>3</TypeDevice>',
        '<UsedFor_Heating>true</UsedFor_Heating>',
        '<UsedFor_DHW>false</UsedFor_DHW>',
        '<UsedFor_Cooling>false</UsedFor_Cooling>',
        '<UsedFor_Ventilation>false</UsedFor_Ventilation>',
        '<UsedFor_Humidification>false</UsedFor_Humidification>',
        '<UsedFor_Dehumidification>false</UsedFor_Dehumidification>',
        '<PH_Parameters>',
        '<EnergySourceBoilerType>1</EnergySourceBoilerType>',
        '<CondensingBoiler>true</CondensingBoiler>',
        '<InConditionedSpace>true</InConditionedSpace>',
        '<MaximalBoilerPower>10.0</MaximalBoilerPower>',
        '<BoilerEfficiency30>0.98</BoilerEfficiency30>',
        '<BoilerEfficiencyNominalOutput>0.94</BoilerEfficiencyNominalOutput>',
        '<AverageReturnTemperatureMeasured30Load>30</AverageReturnTemperatureMeasured30Load>',
        '<AverageBoilerTemperatureDesign70_55>41</AverageBoilerTemperatureDesign70_55>',
        '<AverageBoilerTemperatureDesign55_45>35</AverageBoilerTemperatureDesign55_45>',
        '<AverageBoilerTemperatureDesign35_28>24</AverageBoilerTemperatureDesign35_28>',
        '<StandbyHeatLossBoiler70>None</StandbyHeatLossBoiler70>',
        '<SolarFractionBoilerSpaceHeating>None</SolarFractionBoilerSpaceHeating>',
        '<AuxiliaryEnergy>None</AuxiliaryEnergy>',
        '<AuxiliaryEnergyDHW>None</AuxiliaryEnergyDHW>',
        '</PH_Parameters>',
        '<DHW_Parameters>',
        '<CoverageWithinSystem>0.0</CoverageWithinSystem>',
        '<Unit>0.0</Unit>',
        '<Selection>1</Selection>',
        '</DHW_Parameters>',
        '<Heating_Parameters>',
        '<CoverageWithinSystem>0.0</CoverageWithinSystem>',
        '<Unit>0.0</Unit>',
        '<Selection>1</Selection>',
        '</Heating_Parameters>',
        '</Device>',
        '</Devices>',
        '<PHDistribution>',
        '<DistributionCooling/>',
        '<UseDefaultValues>true</UseDefaultValues>',
        '<DeviceInConditionedSpace>true</DeviceInConditionedSpace>',
        '</PHDistribution>',
        '</System>',
        '</Systems>']
