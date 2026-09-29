/* EduARexx M1 example - MIT License */
parse upper arg command rest

select
  when command = 'INFO' then call info
  when command = 'COUNT' then call count rest
  when command = 'GREET' then say greeting(rest)
  when command = 'HELP' | command = '' then call help
  otherwise do
    say 'Ukjent kommando:' command
    call help
    exit 10
  end
end
exit 0

info:
  say 'EduARexx PowerTool M1'
  return

count: procedure
  parse arg maximum
  if maximum = '' then maximum = 5
  do i = 1 to maximum
    say i
  end
  return

greeting: procedure
  parse arg name
  if name = '' then name = 'Amiga-bruker'
  return 'Hei,' name || '!'

help:
  say 'INFO | COUNT n | GREET navn | HELP'
  return
