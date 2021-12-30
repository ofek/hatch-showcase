# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import click

from hatch_showcase.__about__ import __version__
from hatch_showcase.fib import fibonacci


@click.version_option(version=__version__, prog_name='hatch-showcase')
@click.group()
def hatch_showcase():
    pass


@click.argument('n', type=int)
@hatch_showcase.command()
def fib(n: int):
    click.echo(fibonacci(n))
