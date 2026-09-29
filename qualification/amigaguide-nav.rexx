/* EduARexx AmigaGuide ARexx navigation probe.
 * Argument 1: AmigaGuide ARexx port name.
 * Emits PASS only after all commands return RC=0.
 */
parse arg port
if port = '' then exit 10
if ~show('P', port) then exit 10

address value port
options results

'LINK Main'
if rc ~= 0 then exit 20
'NEXT'
if rc ~= 0 then exit 20
'PREVIOUS'
if rc ~= 0 then exit 20
'RETRACE'
if rc ~= 0 then exit 20

say 'EDUAREXX_AREXX_NAVIGATION=PASS'

'QUIT'
if rc ~= 0 then exit 20
exit 0
