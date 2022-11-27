import click
from humai_desarrollo import my_etl as etl


@click.command()
@click.option("--number", type=int, prompt="Elegi un numero", help="El numero elegido.")
def main(number):
    """Elegis un numero y te devuelve un texto asociado"""
    number, data = etl.number_api_extract(number)
    print(data)
    df = etl.load(number, data)
    etl.transform(df)


if __name__ == "__main__":
    main()
