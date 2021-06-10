import database.db_func as db


'''
db.addUser("Elon", "Musk", "Rocketman", "Ihearttesla", "elon@neural.net", 1);
db.addUser("Jeff", "Bezos", "TheBookyman", "1daydelivery", "bezos@amazon.com", 1);
db.addUser("Han", "Solo", "Falcon1", "Iknow", "han@space.net", 0);
db.addUser("Chewy", "Bacca", "OG", "millfalc", "chewdog@space.web", 0);
db.addUser("Leroy", "Jenkins", "LJ", "CHARGE", "leroy@wow.com", 0);

db.setUsername("TheBookyman", "BookMaster2000");


db.addFollow("Rocketman", "BookMaster2000");
db.addFollow("Falcon1", "BookMaster2000");
db.addFollow("OG", "BookMaster2000");
db.addFollow("BookMaster2000", "OG");

db.addPost("OG" , "Dancing in the Moonlight", "King Harvest", "https.song.link", "https.image.link", "This song is so underrated. I love this song so much")
'''
#db.addPost("OG" , "Dancing in the Dark", "Bruce Springsteen", "https.track.link", "https.pic.link", "Does dancing in moonlight count as dancing in the dark?");

#db.addDM("OG", "LJ", "I'm so glad you like that song")
#db.addDM("LJ", "OG", "Totally. I've been listening to that song since I was little")
#db.addDM("OG", "LJ", "Ever heard of 'Into The Deep'? It's really good too")
#db.addDM("OG", "LJ", "A little different and newer though")
#db.addDM("OG", "Rocketman", "I bet you do some dancin in the moonlight")


#db.addComment("LJ", 5, "OMG I love this song!!!!")

#print(db.getPassword("LJ"));

#db.deleteUser("Rocketman");

#db.setFname("Rocketman", "Elron")

#print(db.usernameTaken("Rocketman"));

#print(db.getAdminStatus("OG"));

#print(db.getFname("Rocketman"))

#db.deleteFollow("OG", "BookMaster2000")

print(db.getImageLink(65))

#array = db.getConvo("OG", "LJ")
#array = db.getFollowers("BookMaster2000")
#array = db.getComments(5)
#array = db.searchPosts("King Harvest")
#for x in array: 
 #   print(x);
'''
array = db.getPosts("OG")
for x in array :
    for y in x:
        print(y)
'''

#print(db.getTimeCreated('d', 5))

#db.addUser("Bill", "Gates", "Bookyman", "Macrosoft", "gates@hotmail.com", 1);

#print(db.searchUsers("Book"));

#pNumArr = db.searchPosts("Dan");
#for x in pNumArr:
#    print(db.getSongTitle(x));