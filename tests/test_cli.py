from citest.cli import main


def test_cli_output(capsys):
    assert main(["1", "2", "3"]) == 0
    assert capsys.readouterr().out.strip() == "mean=2 median=2 rms=2.16025"
