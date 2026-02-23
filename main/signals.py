from django.dispatch import Signal, receiver

from .utilities import send_activation_notification, \
    send_new_comment_notification

post_register = Signal()
comment_saved = Signal()

@receiver(post_register)
def post_register_dispatcher(sender, **kwargs):
    send_activation_notification(kwargs['request'], kwargs['user'])

@receiver(comment_saved)
def post_save_dispatcher(sender, **kwargs):
    comment = kwargs['comment']
    if comment.bb.author.send_messages:
        send_new_comment_notification(kwargs['request'], comment)
