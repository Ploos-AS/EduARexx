/* EduARexx M2 example - MIT License */
parse upper arg command rest

select
  when command = 'INFO' then call systeminfo
  when command = 'LIST' then call listpath rest
  when command = 'CHECK' then call checksystem
  when command = 'HELP' | command = '' then call help
  otherwise do
    say 'Ukjent kommando:' command
    call help
    exit 10
  end
end
exit 0

systeminfo:
  address command 'INFO'
  call checkrc 'INFO'
  return

listpath: procedure expose RC
  parse arg path
  if path = '' then do
    say 'LIST krever en sti.'
    exit 10
  end
  address command 'LIST' path
  call checkrc 'LIST'
  return

checksystem:
  say 'Kontrollerer RAM:'
  address command 'LIST RAM:'
  call checkrc 'LIST RAM:'
  say 'Systemkontroll ferdig.'
  return

checkrc: procedure expose RC
  parse arg operation
  if RC ~= 0 then do
    say operation 'feilet. RC =' RC
    exit RC
  end
  return

help:
  say 'INFO | LIST sti | CHECK | HELP'
  return
