from typer.testing import CliRunner

from cli import app

runner = CliRunner()


def test_cost():
    result = runner.invoke(
        app,
        [
            "cost",
            "--base-delivery-price",
            100,
            "--package-details",
            "PKG1 5 5 OFR001",
            "--package-details",
            "PKG2 15 5 OFR002",
            "--package-details",
            "PKG3 10 100 OFR003",
        ],
    )
    assert result.exit_code == 0
    output = result.stdout.split("\n")
    assert output[0] == "PKG1 0 175"
    assert output[1] == "PKG2 0 275"
    assert output[2] == "PKG3 35 665"


def test_time():
    result = runner.invoke(
        app,
        [
            "time",
            "--base-delivery-price",
            100,
            "--package-details",
            "PKG1 50 30 OFR001",
            "--package-details",
            "PKG2 75 125 OFFR0008",
            "--package-details",
            "PKG3 175 100 OFFR003",
            "--package-details",
            "PKG4 110 60 OFFR002",
            "--package-details",
            "PKG5 155 95 NA",
            "--vehicle-details",
            2,
            70,
            200,
        ],
    )
    assert result.exit_code == 0
    output = result.stdout.split("\n")
    assert output[0] == "PKG1 0 750 3.98"
    assert output[1] == "PKG2 0 1475 1.78"
    assert output[2] == "PKG3 0 2350 1.42"
    assert output[3] == "PKG4 105 1395 0.85"
    assert output[4] == "PKG5 0 2125 4.19"
