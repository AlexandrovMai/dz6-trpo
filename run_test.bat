python rabitmq_ctl.py "myqueue" "send" "message1"
python rabitmq_ctl.py "myqueue" "send" "message2"
python rabitmq_ctl.py "myqueue" "send" "message3"

timeout /t 5 /nobreak

python rabitmq_ctl.py "myqueue" "recv" "3"