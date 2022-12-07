from PHX.model.hvac import collection, heating, cooling, water, ventilation
import pytest


def test_default_PhxMechanicalEquipmentCollection(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    c2 = collection.PhxMechanicalSystemCollection()

    assert c1.id_num == 1
    assert c2.id_num == 2

    assert not c1.devices
    assert not c2.devices


def test_get_mech_device_by_key(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    vent_device = ventilation.PhxDeviceVentilator()
    c1.add_new_mech_device(vent_device.identifier, vent_device)

    assert c1.device_in_collection(vent_device.identifier)
    d = c1.get_mech_device_by_key(vent_device.identifier)
    assert d == vent_device


def test_get_mech_device_by_NONE_key(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    sys = c1.get_mech_device_by_key("")
    assert sys is None


def test_get_mech_device_by_id(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    vent_device = ventilation.PhxDeviceVentilator()
    c1.add_new_mech_device(vent_device.identifier, vent_device)

    assert c1.device_in_collection(vent_device.identifier)
    d = c1.get_mech_device_by_id(vent_device.id_num)
    assert d == vent_device


def test_get_mech_device_by_NONE_id(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    with pytest.raises(collection.NoVentUnitFoundError):
        c1.get_mech_device_by_id(999_999_999)


# -- Ventilation
def test_add_ventilation_device(reset_class_counters):
    c1 = collection.PhxMechanicalSystemCollection()
    vent_device = ventilation.PhxDeviceVentilator()
    c1.add_new_mech_device(vent_device.identifier, vent_device)

    assert c1.device_in_collection(vent_device.identifier)
    assert not c1.device_in_collection("not_a_key")


def test_get_ventilation_device():
    c1 = collection.PhxMechanicalSystemCollection()
    vent_device = ventilation.PhxDeviceVentilator()
    c1.add_new_mech_device(vent_device.identifier, vent_device)

    assert vent_device in c1.ventilation_devices


# TODO: Finish Mech Collection Tests
# -- Heating

# -- Cooling

# -- DHW

# -- DHW Recric Piping

# -- DHW Branch Piping
