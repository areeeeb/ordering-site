import json

from channels.generic.websocket import AsyncWebsocketConsumer


ROOM_NAME = 'admin_orders_list'


class OrdersConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # join room group
        await self.channel_layer.group_add(
            ROOM_NAME,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # leave room group
        await self.channel_layer.group_discard(
            ROOM_NAME,
            self.channel_name
        )

    # Receive message from websocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        order = text_data_json['order']

        # Send message to room group
        await self.channel_layer.group_send(
            ROOM_NAME,
            {
                'type': 'send_order',
                'order': order
            }
        )

    # Receive message from the group
    async def send_order(self, event):
        order = event['order']
        await self.send(text_data=json.dumps({
            'order': order
        }))
