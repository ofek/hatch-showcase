# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import click

from hatch_showcase._version import version
from hatch_showcase.fib import fibonacci


# NOTE: The group/command decorators must come last to avoid the following issue at runtime:
# https://github.com/pallets/click/issues/1199


@click.version_option(version=version, prog_name='hatch-showcase')
@click.group()
def hatch_showcase():
    pass


@click.argument('n', type=int)
@hatch_showcase.command()
def fib(n: int):
    click.echo(fibonacci(n))
