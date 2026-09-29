/* EduARexx AmigaGuide ARexx navigation probe.
 * Args: primary-port [secondary-port] [BASE|V40]
 * BASE: LINK Main + QUIT.
 * V40: additionally NEXT/PREVIOUS/RETRACE on secondary port.
 */
parse arg primary secondary mode
if primary = '' then exit 10
if mode = '' then mode = 'BASE'
mode = translate(mode)

if ~show('P', primary) then exit 10

address value primary
options results
'LINK Main'
if rc ~= 0 then exit 20
say 'EDUAREXX_MAIN_NODE=PASS'

if mode = 'V40' then do
  if secondary = '' then exit 10
  if ~show('P', secondary) then exit 10
  address value secondary
  'NEXT'
  if rc ~= 0 then exit 20
  'PREVIOUS'
  if rc ~= 0 then exit 20
  'RETRACE'
  if rc ~= 0 then exit 20
  say 'EDUAREXX_AREXX_NAVIGATION_V40=PASS'
end
else do
  if mode ~= 'BASE' then exit 10
  say 'EDUAREXX_AREXX_NAVIGATION_BASE=PASS'
end

address value primary
'QUIT'
if rc ~= 0 then exit 20
say 'EDUAREXX_AMIGAGUIDE_QUIT=PASS'
exit 0
