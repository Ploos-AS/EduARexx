# AmigaGuide launcher build

The native qualification launcher is source-only in this repository.

Build it with the Ploos-AS `amiga-dev` Bebbo m68k toolchain:

```sh
sh tools/build_amigaguide_launcher.sh
```

The expected compiler command is `m68k-amigaos-gcc`; override it with `M68K_CC` when the toolchain exposes another path.

A source commit or Linux syntax check is **not** a native compile PASS. Qualification requires the actual Amiga m68k compiler/NDK and later execution on classic AmigaOS.
