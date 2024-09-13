from unittest.mock import patch

import pytest
from fastapi import HTTPException

from guruxone.models import DBAchievement, DBMember, DBPayment
from guruxone.routes.members import (
    get_all_members,
    get_meber_by_id,
    get_member_achievements,
    get_member_payments,
)


@patch("guruxone.routes.members.get_db_members", return_value=list[DBMember])
def test_get_all_members(mock_get_db_members):
    """Return the list of members found in the database"""
    assert get_all_members("Fake_db") is mock_get_db_members.return_value
    mock_get_db_members.assert_called_with("Fake_db")


@patch("guruxone.routes.members.get_db_member_by_id", return_value=DBMember)
def test_get_meber_by_id(mock_get_db_member_by_id):
    """Returns the Member with the specified id"""
    assert get_meber_by_id(id=13, db="Fake db") is mock_get_db_member_by_id.return_value
    mock_get_db_member_by_id.assert_called_with(13, "Fake db")


@patch("guruxone.routes.members.get_db_member_by_id", return_value=None)
def test_get_meber_by_id_404(_):
    """Raises HttpException with 404 when no event is found"""
    with pytest.raises(HTTPException):
        get_meber_by_id(id=0, db=None)


@patch("guruxone.routes.members.get_db_member_payments", return_value=list[DBPayment])
def test_get_member_payments(mock_get_db_member_payments):
    """Returns the list of payments for Member with the specified id"""
    assert (
        get_member_payments(id=13, db="Fake db")
        is mock_get_db_member_payments.return_value
    )
    mock_get_db_member_payments.assert_called_with(13, "Fake db")


@patch(
    "guruxone.routes.members.get_db_member_achivements",
    return_value=list[DBAchievement],
)
def test_get_member_achievements(mock_get_db_member_achivements):
    """Returns the list of achievements for Member with the specified id"""
    assert (
        get_member_achievements(id=13, db="Fake db")
        is mock_get_db_member_achivements.return_value
    )
    mock_get_db_member_achivements.assert_called_with(13, "Fake db")
