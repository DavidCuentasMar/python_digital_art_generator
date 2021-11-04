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
@click.option(
    '--author',
    default=None,
    help='Name of the author',
    required=False
)
def main(output_name,author):
    """Main function"""
    Controller.worker(output_name,author)
    os._exit(os.EX_OK)


cli.add_command(main)
if __name__ == '__main__':
    cli()