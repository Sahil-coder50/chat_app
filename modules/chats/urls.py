from django.urls import path
from rest_framework import routers
from modules.chats.views import *

router = routers.DefaultRouter()

router.register(r"conversations", ConversationViewSet, basename="conversations")
# router.register(r"messages", MessageViewSet, basename="messages")
# router.register(r"uploads", UploadViewSet, basename="uploads")

urlpatterns = [] + router.urls


"""
Conversations
List conversations
GET /api/conversations/

Response:

[
  {
    "id": 1,
    "type": "direct",
    "last_message": {
      "id": 50,
      "content": "Hello"
    },
    "unread_count": 3
  }
]
Get conversation details
GET /api/conversations/1/
Create DM
POST /api/conversations/direct/

Body:

{
  "user_id": 15
}
Create group
POST /api/conversations/group/

Body:

{
  "title": "Backend Team",
  "members": [1,2,3,4]
}
Members
Add member
POST /api/conversations/1/members/

Body:

{
  "user_id": 25
}
Remove member
DELETE /api/conversations/1/members/25/
List members
GET /api/conversations/1/members/
Messages

This is the most important area.

List messages
GET /api/conversations/1/messages/

Pagination:

GET /api/conversations/1/messages/?cursor=xyz

Never load all messages.

Send message
POST /api/conversations/1/messages/

Body:

{
  "content": "Hello"
}

Response:

{
  "id": 100,
  "content": "Hello"
}
Get single message
GET /api/messages/100/
Edit message
PATCH /api/messages/100/

Body:

{
  "content": "Updated text"
}
Delete message
DELETE /api/messages/100/

Usually soft-delete.

Reply

Can be handled inside send message.

POST /api/conversations/1/messages/

Body:

{
  "content": "Sure",
  "reply_to": 55
}

No separate endpoint needed.

Attachments
Upload file

Option A (recommended)

POST /api/uploads/

multipart form-data

Response:

{
  "file_id": "abc123",
  "url": "..."
}

Then:

POST /api/conversations/1/messages/
{
  "content": "",
  "attachments": ["abc123"]
}
Download attachment
GET /api/attachments/55/
Reactions
Add/Change reaction
POST /api/messages/100/reactions/

Body:

{
  "emoji": "👍"
}
Remove reaction
DELETE /api/messages/100/reactions/👍/

or

DELETE /api/messages/100/reactions/

Body:

{
  "emoji": "👍"
}
Read Receipts

If using last_read_message.

Mark conversation as read
POST /api/conversations/1/read/

Body:

{
  "last_read_message_id": 100
}

Backend updates:

Participants.last_read_message = 100

That's all.

Get unread count

Usually returned in:

GET /api/conversations/

No separate endpoint needed.

Search
GET /api/search/messages/?q=hello

or

GET /api/conversations/1/search/?q=invoice
Presence

Usually websocket + Redis.

User online
{
  "type": "presence",
  "user_id": 5,
  "status": "online"
}

No REST endpoint required.

Typing

WebSocket only.

{
  "type": "typing",
  "conversation_id": 1,
  "is_typing": true
}
"""


"""
WebSocket Events

A production app typically has one websocket connection.

ws/chat/

Events:

New message
{
  "type": "message.created"
}
Message edited
{
  "type": "message.updated"
}
Message deleted
{
  "type": "message.deleted"
}
Reaction
{
  "type": "reaction.created"
}
Read receipt
{
  "type": "message.read"
}
Typing
{
  "type": "typing"
}
Presence
{
  "type": "presence"
}
"""