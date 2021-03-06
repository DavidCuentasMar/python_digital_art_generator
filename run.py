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
@click.option(
    '--output_name',
    default="digital_art",
    help='Name of the output images',
    required=False
)
def main(output_name):
    """Main function"""
    Controller.worker(output_name)
    os._exit(os.EX_OK)


cli.add_command(main)
if __name__ == '__main__':
    cli()