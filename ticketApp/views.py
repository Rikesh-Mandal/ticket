from rest_framework.response import Response
from rest_framework.decorators import api_view
<<<<<<< HEAD
from .serializers import TicketSerializer, ReplySerializer
from .models import Ticket, Reply
=======
from .serializers import TicketSerializer
from .models import Ticket
>>>>>>> new_branch
from rest_framework import status


# Create your views here.
@api_view(['GET', 'POST'])
def ticket_list(request):
    if request.method == 'GET':
        tickets = Ticket.objects.all()
        serializer = TicketSerializer(tickets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TicketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def ticket_details(request, ticket_id):
    try:
        tickets = Ticket.objects.get(pk=ticket_id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TicketSerializer(tickets)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TicketSerializer(tickets, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        tickets.delete()
<<<<<<< HEAD
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def ticket_replies(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    replies = Reply.objects.filter(ticket=ticket)
    serializer = ReplySerializer(replies, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def create_reply(request, ticket_id):
    try:
        ticket = Ticket.objects.get(pk=ticket_id)
    except Ticket.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {
        'ticket': ticket.id,
        'comment': request.data.get('comment')
    }

    serializer = ReplySerializer(data=data)
    if serializer.is_valid():
        serializer.save(ticket=ticket)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'DELETE'])
def update_delete_reply(request, ticket_id, reply_id):
    try:
        reply = Reply.objects.get(ticket_id=ticket_id, pk=reply_id )
    except Reply.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    data = {
        'ticket': ticket_id,
        'comment': request.data.get('comment')
    }

    if request.method == 'PUT':
        serializer = ReplySerializer(reply, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        reply.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
=======
        return Response(status=status.HTTP_204_NO_CONTENT)
>>>>>>> new_branch
