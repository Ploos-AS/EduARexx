/* EduARexx M5 client - MIT License */
options results

address EDUHOST 'PING'
say 'PING: RC=' RC 'RESULT=' RESULT

address EDUHOST 'VERSION'
say 'VERSION: RC=' RC 'RESULT=' RESULT

address EDUHOST 'ECHO hello from ARexx'
say 'ECHO: RC=' RC 'RESULT=' RESULT

address EDUHOST 'ADD 2 3'
say 'ADD: RC=' RC 'RESULT=' RESULT

exit 0
