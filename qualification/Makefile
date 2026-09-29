CC = m68k-amigaos-gcc
CFLAGS ?= -Os -Wall -Wextra
OUT ?= ../build/amigaguide-launcher

.PHONY: all clean
all: $(OUT)

$(OUT): amigaguide-launcher.c
	mkdir -p ../build
	$(CC) $(CFLAGS) -o $(OUT) amigaguide-launcher.c -lamigaguide

clean:
	rm -f $(OUT)
