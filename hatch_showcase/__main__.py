# SPDX-FileCopyrightText: 2021-present Ofek Lev <oss@ofek.dev>
#
# SPDX-License-Identifier: MIT
import sys

if __name__ == '__main__':
    from .cli import hatch_showcase

    sys.exit(hatch_showcase())
