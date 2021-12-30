# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
from hatch_showcase.fib import fibonacci


def test():
    assert fibonacci(32) == 2178309
