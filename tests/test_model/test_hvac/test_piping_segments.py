import pytest

from ladybug_geometry.geometry3d.pointvector import Point3D
from ladybug_geometry.geometry3d.polyline import LineSegment3D
from PHX.model.hvac.piping import (
    PhxPipeSegment,
    PhxHotWaterPipingMaterial,
    PhxHotWaterPipingDiameter,
)


def test_PhxPipeSegment_heat_loss_coefficient_1():
    p1, p2 = Point3D(0, 0, 0), Point3D(0, 0, 1)
    geom = LineSegment3D(p1, p2)

    seg = PhxPipeSegment(
        identifier="test",
        display_name="test",
        geometry=geom,
        pipe_material=PhxHotWaterPipingMaterial.COPPER_K,
        pipe_diameter=PhxHotWaterPipingDiameter._1_0_0_IN,
        insulation_thickness_m=0.0254,
        insulation_conductivity=0.04,
        insulation_reflective=True,
        insulation_quality=None,
        daily_period=24,
    )

    k2 = seg._solve_for_pipe_heat_loss_coeff()
    assert k2 == pytest.approx(0.18920200481210636)


def test_PhxPipeSegment_heat_loss_coefficient_2():
    p1, p2 = Point3D(0, 0, 0), Point3D(0, 0, 1)
    geom = LineSegment3D(p1, p2)

    seg = PhxPipeSegment(
        identifier="test",
        display_name="test",
        geometry=geom,
        pipe_material=PhxHotWaterPipingMaterial.COPPER_K,
        pipe_diameter=PhxHotWaterPipingDiameter._1_0_0_IN,
        insulation_thickness_m=0.0254,
        insulation_conductivity=0.04,
        insulation_reflective=False,
        insulation_quality=None,
        daily_period=24,
    )

    k2 = seg._solve_for_pipe_heat_loss_coeff()
    assert k2 == pytest.approx(0.21003911131648087)
