import click
from datetime import datetime


@click.command()
@click.option("--number", type=int, prompt="Elegi un numero", help="El numero elegido.")
def main(number):
    """Elegis un numero y te devuelve un texto asociado"""
    number_text = number_api(number)
    print(number_text)


if __name__ == "__main__":
    main()
