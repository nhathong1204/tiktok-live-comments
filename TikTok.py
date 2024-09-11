from TikTokLive import TikTokLiveClient
from TikTokLive.events import ConnectEvent, CommentEvent

client = TikTokLiveClient(unique_id="@chedauden96")


def on_connect(event):
    print("Connected to @{} (Room ID: {})".format(event.unique_id, client.room_id))

def on_comment(event):
    print("{}: {}".format(event.user.nickname, event.comment))

client.on(ConnectEvent, on_connect)
client.on(CommentEvent, on_comment)

if __name__ == '__main__':
    client.run()
