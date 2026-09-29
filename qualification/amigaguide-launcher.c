/* EduARexx native AmigaGuide qualification launcher.
 * Classic m68k AmigaOS / NDK. No ROM or AmigaOS files are redistributed.
 */
#include <exec/types.h>
#include <exec/ports.h>
#include <libraries/amigaguide.h>
#include <proto/amigaguide.h>
#include <proto/exec.h>
#include <stdio.h>
#include <string.h>

struct Library *AmigaGuideBase;

static int write_port_name(const char *base) {
    struct MsgPort *port;
    const char *name = NULL;
    FILE *fp;

    Forbid();
    for (port = (struct MsgPort *)SysBase->PortList.lh_Head;
         port->mp_Node.ln_Succ != NULL;
         port = (struct MsgPort *)port->mp_Node.ln_Succ) {
        if (port->mp_Node.ln_Name != NULL &&
            strncmp(port->mp_Node.ln_Name, base, strlen(base)) == 0) {
            name = port->mp_Node.ln_Name;
            break;
        }
    }

    fp = fopen("TEST:results/amigaguide.port", "w");
    if (fp != NULL && name != NULL) {
        fputs(name, fp);
        fputc('\n', fp);
    }
    if (fp != NULL) fclose(fp);
    Permit();

    return name != NULL ? 0 : 20;
}

int main(void) {
    struct NewAmigaGuide nag;
    AMIGAGUIDECONTEXT ctx;
    struct AmigaGuideMsg *msg;
    ULONG sigmask;
    BOOL running = TRUE;

    memset(&nag, 0, sizeof(nag));
    AmigaGuideBase = OpenLibrary("amigaguide.library", 34);
    if (!AmigaGuideBase) return 20;

    nag.nag_Name = (STRPTR)"TEST:EduARexx.guide";
    nag.nag_ClientPort = (STRPTR)"EDUAREXXGUIDE";
    ctx = OpenAmigaGuideAsync(&nag, TAG_DONE);
    if (!ctx) {
        CloseLibrary(AmigaGuideBase);
        return 20;
    }

    if (write_port_name("EDUAREXXGUIDE") != 0) {
        CloseAmigaGuide(ctx);
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
