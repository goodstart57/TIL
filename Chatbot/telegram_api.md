# Telegram chatbot



## Making requests

All queries to the Telegram Bot API must be served over HTTPS and need to be presented in this form: `https://api.telegram.org/bot<token>/METHOD_NAME`. 

```
# Form Example

https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
```



## METHOD NAMES

| name        | info                              |
| ----------- | --------------------------------- |
| getMe       | Account Information               |
| getUpdates  | Messages updated for my bot infor |
| sendMessage | Can Send Message                  |
| setWebhook  | set webhook to my chatbot         |



### HOW TO USE METHOD

- #### __getMe__

```
# getMe example

https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getMe
```



#### __`getMe` returns__

| key    | value                                     |
| ------ | ----------------------------------------- |
| ok     | Whether the request was successful or not |
| result | account information json data             |

__upper result json data__

| key        | value          |
| ---------- | -------------- |
| id         | bot_id         |
| is_bot     | true           |
| first_name | "ssafy-js"     |
| username   | "ssafy_js_bot" |



<br>



- #### __getUpdates__

```
# getUpdates example

https://api.telegram.org/bot123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11/getUpdates
```



__`getUpdates` returns__

| key    | value                                     |
| ------ | ----------------------------------------- |
| ok     | Whether the request was successful or not |
| result | Message logs data                         |



there are account information sendng messages, chat informations, date and message text in result 

for example,

```
{ "ok": true,
  "result": [{
    "update_id": <update_id>,
    "message": {
      "message_id": 1,
      "from": { "id": <user_id>, "is_bot": false, "first_name": "JS", "last_name": "Lee"},
      "chat": { "id": <bot_id>, "first_name": "JS", "last_name": "Lee", "type": "private"},
      "date": 1545119445,
      "text": "/start",
      "entities": [{ "offset": 0, "length": 6, "type": "bot_command"}]
    }
  }]
}
```

<br>

#### __`sendMessage` returns__

`sendMessage` Method returns the same data as `getUpdates`, like ok, result... and account id, chat id in result 