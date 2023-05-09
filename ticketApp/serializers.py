from rest_framework import serializers
<<<<<<< HEAD
from .models import Ticket, Reply


class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Reply
        fields = '__all__'
=======
from .models import Ticket
>>>>>>> new_branch


class TicketSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ticket
        fields = '__all__'

