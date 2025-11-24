import socket
import pytest
from app.models.calculation import Addition, Calculation
from app.database import SessionLocal


def is_docker_db_running():
    try:
        socket.gethostbyname("db")
        return True
    except socket.error:
        return False


@pytest.mark.skipif(not is_docker_db_running(), reason="Docker DB is not running")
def test_db_insert_and_read():
    session = SessionLocal()

    calc = Addition(
        user_id=None,
        inputs=[10, 5]
    )
    calc.result = calc.get_result()

    session.add(calc)
    session.commit()
    session.refresh(calc)

    fetched = session.query(Calculation).filter_by(id=calc.id).first()

    assert fetched is not None
    assert fetched.type == "addition"
    assert fetched.inputs == [10, 5]
    assert fetched.result == 15

    session.close()