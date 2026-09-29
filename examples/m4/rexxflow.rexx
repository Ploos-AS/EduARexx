/* EduARexx M4 example - MIT License */
options results
parse arg command rest
exitcode = 0

if command = '' then command = 'HELP'

select
  when upper(command) = 'HELP' then call help
  when upper(command) = 'CHECK' then call checksystem
  when upper(command) = 'PORT' then call portcommand rest
  otherwise call fail 10, 'Ukjent kommando: ' || command
end

call cleanup
exit exitcode

checksystem:
  call log 'INFO', 'Kontrollerer RAM:'
  address command 'LIST RAM:'
  if RC ~= 0 then call fail RC, 'LIST RAM: feilet'
  call log 'INFO', 'Systemkontroll OK'
  return

portcommand:
  parse arg port command
  if port = '' | command = '' then call fail 10, 'PORT krever port og kommando'
  call log 'INFO', 'Sender kommando til ' || port
  address value port
  command
  status = RC
  answer = RESULT
  if status ~= 0 then call fail status, 'Portkommando feilet'
  if answer ~= '' then say 'RESULT:' answer
  return

fail:
  parse arg code, message
  call log 'ERROR', message
  exitcode = code
  signal cleanup

cleanup:
  call log 'INFO', 'Cleanup'
  exit exitcode

log:
  parse arg level, message
  say '['level']' message
  return

help:
  say 'HELP | CHECK | PORT port command'
  return
