/* EduARexx native AmigaGuide qualification launcher.
 * Target: classic m68k AmigaOS / NDK.
 * Opens the guide asynchronously with a deterministic ARexx client-port base.
 */
#include <exec/types.h>
#include <libraries/amigaguide.h>
#include <proto/amigaguide.h>
#include <proto/exec.h>
#include <proto/dos.h>
#include <stdio.h>
#include <string.h>

struct Library *AmigaGuideBase;

int main(void) {
    struct NewAmigaGuide nag;
    AMIGAGUIDECONTEXT ctx;
    memset(&nag, 0, sizeof(nag));
    AmigaGuideBase = OpenLibrary("amigaguide.library", 34);
    if (!AmigaGuideBase) { puts("EDUAREXX_LAUNCHER_LIBRARY=FAIL"); return 20; }
    nag.nag_Name = "TEST:EduARexx.guide";
    nag.nag_ClientPort = "EDUAREXXGUIDE";
    nag.nag_Client = NULL;
    ctx = OpenAmigaGuideAsync(&nag, TAG_DONE);
    if (!ctx) { puts("EDUAREXX_LAUNCHER_OPEN=FAIL"); CloseLibrary(AmigaGuideBase); return 20; }
    puts("EDUAREXX_LAUNCHER_OPEN=PASS");
    /* Keep the async context alive while the external ARexx probe runs.
       Runtime integration will replace this bounded delay with message handling. */
    Delay(250);
    CloseAmigaGuide(ctx);
    CloseLibrary(AmigaGuideBase);
    return 0;
}
