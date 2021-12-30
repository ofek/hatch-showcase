# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT


def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)
