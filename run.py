import os
import click
import logging
from controller.controller import Controller

# Configuraciones
sh = logging.StreamHandler()
logging.basicConfig(
    format='%(asctime)s |%(name)s|%(levelname)s|%(message)s',
    level=logging.DEBUG,
    handlers=[sh]
)

@click.group()
def cli():
    """Metodo cli."""
    pass


@click.command()
def main():
    """Main function"""
    Controller.worker()
    os._exit(os.EX_OK)


cli.add_command(main)
if __name__ == '__main__':
    cli()