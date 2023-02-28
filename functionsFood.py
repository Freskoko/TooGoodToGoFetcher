from tgtg import TgtgClient
import time

bigone = []

def LogInRefresh(emailUse):

    client = TgtgClient(email=emailUse)
    credentials = client.get_credentials()
    print(credentials)

    with open("creds.txt", "w") as file:
        for i in [credentials["access_token"],credentials["refresh_token"],credentials["user_id"]]:
            file.write(f"{i}\n")

    #TODO = SET SOME TO FAVIOURTE AND THEN CHECK IF AVAIBLE EVERY 5 MINS

def lookforfood():

    with open("creds.txt", "r") as file:
        lines = file.read().splitlines() 

    client = TgtgClient(
        access_token= lines[0], 
        refresh_token= lines[1], 
        user_id= lines[2]
        )

    items = client.get_items(
        favorites_only=False,
        latitude=60.386166,
        longitude=5.324775,
        radius=50,
    )
    for i in items:
        id = i["item"]['item_id']
        dis = i["display_name"]
        itemsav = i['items_available']
        if itemsav > 0:
            # print(i)
            print(f" {id:<10} {dis:<55} {itemsav}  \n")
            bigone.append(f" {id:<10} {dis:<55} {itemsav}  \n")

    client.set_favorite(item_id=896159, is_favorite=True)
    client.set_favorite(item_id=15389, is_favorite=True)

    if bigone == []:
        return None

    return  bigone

if __name__ == "__main__":
    LogInRefresh("frishcoco@gmail.com")
    time.sleep(20)
    print(lookforfood())


#foodora market = 896159
#brasila = 