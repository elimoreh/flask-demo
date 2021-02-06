import click
from click.testing import CliRunner

def test_seed():
    @click.command('python3 seed.py')
    def seed_db():
        click.echo(f"python3 seed.py --total 150")

    runner = CliRunner()
    result = runner.invoke(seed_db)
    assert result.exit_code == 0

