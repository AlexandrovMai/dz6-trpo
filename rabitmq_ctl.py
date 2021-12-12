import pika
import sys

# use like: python3 rabitmq_ctl.py <queue_name> send <message>
#           python3 rabitmq_ctl.py <queue_name> recv <msg_count>

queue = sys.argv[1]
msg_count = 0
msg_limit = 0

connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost'))
channel = connection.channel()
channel.queue_declare(queue=queue)


def send_message():
    channel.basic_publish(exchange='',
                          routing_key=queue,
                          body=sys.argv[3])


def stop_consume():
    channel.stop_consuming()


def on_message(ch, method, properties, body):
    global msg_count
    print("Received message on: ", ch, "Body:", body)
    msg_count += 1
    if msg_count == msg_limit:
        stop_consume()


def recv_message():
    channel.basic_consume(on_message_callback=on_message, queue=queue, auto_ack=True)
    channel.start_consuming()


if sys.argv[2] == "send":
    print("Sending message for queue", queue, sys.argv[3])
    send_message()
else:
    msg_limit = int(sys.argv[3])
    recv_message()
connection.close()
