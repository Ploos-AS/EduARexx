#!/bin/sh
set -eu
CC=${M68K_CC:-m68k-amigaos-gcc}
OUT=${1:-build/amigaguide-launcher}
mkdir -p "$(dirname "$OUT")"
command -v "$CC" >/dev/null 2>&1 || { echo "missing Bebbo compiler: $CC" >&2; exit 69; }
"$CC" -Os -Wall -Wextra -o "$OUT" qualification/amigaguide-launcher.c -lamigaguide
echo "Built $OUT"
