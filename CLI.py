import click

from homework.patient import Patient, PatientCollection


@click.group()
def cli():
    pass

@cli.command()
@click.argument("first_name")
@click.argument("last_name")
@click.option("--birth-date", help="Birth day")
@click.option("--phone", help="Phone")
@click.option("--document-type", help="Document type")
@click.option("--document-number", help="Document id")
def create(first_name, last_name, birth_date, phone, document_type, document_number):
    par = Patient.create(first_name, last_name, birth_date, phone, document_type, document_number)
    print(par.save())
    click.echo(par)


@cli.command()
@click.option("--val", default=10, help="limit")
def show(val):
    Pc = PatientCollection()
    for pat in Pc.limit(val):
        click.echo(pat)


@cli.command()
def count():
    click.echo(PatientCollection().count())
    # print(PatientCollection().count())
#
#
# cli.command(create)
# cli.command(show)
# cli.command(count)

cli()
# if __name__ == 'main':
#     pass
