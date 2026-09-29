/*
 * EduARexx EDUHOST
 * MIT License
 *
 * M5 qualification skeleton.
 *
 * This file intentionally documents architecture before binding the course
 * to unverified SDK/ABI details. The native implementation must be completed
 * and compiled against the Amiga m68k development headers used by the
 * project's qualified toolchain.
 */

#include <stdio.h>
#include <string.h>

static int dispatch_command(const char *command)
{
    if (command == NULL)
        return 10;

    if (strcmp(command, "PING") == 0) {
        puts("PONG");
        return 0;
    }

    if (strcmp(command, "VERSION") == 0) {
        puts("EDUHOST M5");
        return 0;
    }

    return 10;
}

int main(void)
{
    /*
     * Qualification TODO:
     *  - open required Amiga libraries
     *  - create/publish EDUHOST Exec message port
     *  - Wait() for RexxMsg traffic
     *  - validate RexxMsg
     *  - dispatch command + arguments
     *  - create ARexx-compatible result
     *  - set return fields
     *  - ReplyMsg()
     *  - remove port and release resources
     */

    puts("EDUHOST M5 qualification skeleton");
    return dispatch_command("PING");
}
