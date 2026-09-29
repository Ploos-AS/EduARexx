/* EduARexx M3 example - MIT License */
options results
parse arg port command

if port = '' | command = '' then do
  say 'Bruk: rx portcommander.rexx PORT COMMAND'
  exit 10
end

address value port
command
status = RC
answer = RESULT

if status ~= 0 then do
  say 'Kommandoen feilet. RC =' status
  exit status
end

say 'OK. RC =' status
if answer ~= '' then say 'RESULT:' answer
exit 0
