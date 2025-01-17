from PHX.model.loads import ventilation as vent_loads


def test_default_vent_load(reset_class_counters):
    vent_load1 = vent_loads.PhxLoadVentilation()
    assert vent_load1


def test_vent_load_has_ventilation(reset_class_counters) -> None:
    vent_load1 = vent_loads.PhxLoadVentilation()
    vent_load1.flow_extract = 1
    vent_load1.flow_supply = 1
    vent_load1.flow_transfer = 1

    assert vent_load1.total_airflow == 3


def test_vent_load_does_not_have_ventilation(reset_class_counters) -> None:
    vent_load1 = vent_loads.PhxLoadVentilation()
    vent_load1.flow_extract = 0
    vent_load1.flow_supply = 0
    vent_load1.flow_transfer = 0

    assert vent_load1.total_airflow == 0
