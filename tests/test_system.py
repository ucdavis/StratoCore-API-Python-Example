"""Tests for the PpmsSystem class."""

import pytest

from pyppms.system import PpmsSystem

__author__ = "Niko Ehrenfeuchter"
__copyright__ = __author__
__license__ = "gpl3"


FMT_DATE = r"%Y-%m-%d"
FMT_TIME = r"%H:%M:%S"
FMT = f"{FMT_DATE} {FMT_TIME}"
DAY = "2019-05-18"
TIME_START = "12:30:00"
TIME_END = "13:15:00"
START = f"{DAY} {TIME_START}"
END = f"{DAY} {TIME_END}"

SYS_ID = "42"
NAME = "Our Brand-New Microscope"
LOC = "The Perfect Microscopy Room"
SYS_TYPE = "Seven-Photon Microscopes"
CORE_REF = "23"
EXPECTED = (
    f"system_id: {SYS_ID}, name: {NAME}, localisation: {LOC}, system_type: {SYS_TYPE}, "
    f"core_facility_ref: {CORE_REF}, schedules: True, active: True, "
    "stats: True, bookable: True, autonomy_required: True, "
    "autonomy_required_after_hours: False"
)


def create_system(system_id=SYS_ID):
    """Helper function to create a PpmsSystem object with default values.

    Returns
    -------
    PpmsSystem
    """
    return PpmsSystem(
        system_id=system_id,
        name=NAME,
        localisation=LOC,
        system_type=SYS_TYPE,
        core_facility_ref=CORE_REF,
        schedules=True,
        active=True,
        stats=True,
        bookable=True,
        autonomy_required=True,
        autonomy_required_after_hours=False,
    )


def test_ppmssystem():
    """Test the PpmsSystem constructor."""
    booking = create_system()

    assert booking.__str__() == EXPECTED


def test_ppmssystem_invalid_id():
    """Test the PpmsSystem constructor raising a ValueError."""
    with pytest.raises(ValueError):
        create_system(system_id="cannot-parse-to-int")
