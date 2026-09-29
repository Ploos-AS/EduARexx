/* EduARexx native AmigaGuide qualification launcher.
 * Classic m68k AmigaOS / NDK. No ROM or AmigaOS files are redistributed.
 */
#include <exec/types.h>
#include <libraries/amigaguide.h>
#include <proto/amigaguide.h>
#include <proto/exec.h>
#include <stdio.h>
#include <string.h>

struct Library *AmigaGuideBase;

int main(void) {
    struct NewAmigaGuide nag;
    AMIGAGUIDECONTEXT ctx;
    struct AmigaGuideMsg *msg;
    ULONG sigmask;
    BOOL running = TRUE;

    memset(&nag, 0, sizeof(nag));
    AmigaGuideBase = OpenLibrary("amigaguide.library", 34);
    if (!AmigaGuideBase) return 20;

    nag.nag_Name = "TEST:EduARexx.guide";
    nag.nag_ClientPort = "EDUAREXXGUIDE";
    ctx = OpenAmigaGuideAsync(&nag, TAG_DONE);
    if (!ctx) {
        CloseLibrary(AmigaGuideBase);
        return 20;
    }

    puts("EDUAREXX_LAUNCHER_OPEN=PASS");
    sigmask = AmigaGuideSignal(ctx);

    while (running) {
        ULONG signals = Wait(sigmask | SIGBREAKF_CTRL_C);
        if (signals & SIGBREAKF_CTRL_C) running = FALSE;

        while ((msg = GetAmigaGuideMsg(ctx)) != NULL) {
            if (msg->agm_Type == ShutdownMsgID) running = FALSE;
            ReplyAmigaGuideMsg(msg);
        }
    }

    CloseAmigaGuide(ctx);
    CloseLibrary(AmigaGuideBase);
    return 0;
}
