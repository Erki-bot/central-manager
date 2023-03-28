import random
a = '{"user_id" : "jack"'+str(random.randint(0,1000))+', "text" : "Ahoy!"}'


curl -X POST -d '{"user_id" : "jack", "text" : "Ahoy!"}' \
  'https://central-manager-4d063-default-rtdb.firebaseio.com/message_list.json'