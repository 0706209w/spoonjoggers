import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pawcrastination_project.settings')

import django
django.setup()

from pawcrastination.models import AnimalProfile, Picture, UserProfile

def populate():
    Bob = add_user("Bob", "email@legit.com", "password", "www.example.com", "profile_images/bobs_pretty_face.png")
    print "add user worked"
    print Bob
    bobs_animal = add_animal("Orlando", owner = Bob, type = "Horses")
    print "add animal worked"
    print bobs_animal
    add_picture(animal = bobs_animal, caption = "My pony", title = "Orlando the Pony", picture = "images/Pony_1.jpg")
    add_picture(animal = bobs_animal, caption = "Check that mane", title = "Orlando the Pony", picture = "images/Pony_2.jpg")
    add_picture(animal = bobs_animal, caption = "He's pretty great", title = "Orlando the Pony", picture = "images/Pony_3.jpg")
    bobs_other_animal = add_animal("Sid", owner = Bob, type = "Reptiles")
    print "add animal worked"
    print bobs_other_animal
    add_picture(animal = bobs_other_animal, caption = "My Snake Sid", title = "Sid the Snake", picture = "images/Snake_1.jpg")
    add_picture(animal = bobs_other_animal, caption = "He's not as good as the pony", title = "Sid the Snake", picture = "images/Snake_2.jpg")
    add_picture(animal = bobs_other_animal, caption = "You can't hug a snake", title = "Sid the Snake", picture = "images/Snake_3.jpg")

    Angela = add_user("Angela", "angie@legit.com", "password", "www.ilovepets.com", "profile_images/Angela.jpg")
    print "add user worked"
    print Angela
    angelas_animal = add_animal("Boo", owner = Angela, type = "Dogs")
    print "add animal worked"
    print angelas_animal
    add_picture(animal = angelas_animal, caption = "this is a fluff", title = "Boo the dog", picture = "images/Boo_1.jpg")
    add_picture(animal = angelas_animal, caption = "seriously he's so fluffy", title = "Boo the dog", picture = "images/Boo_2.jpg")
    add_picture(animal = angelas_animal, caption = "lil fluff", title = "Boo the dog", picture = "images/Boo_3.jpg")
    angelas_other_animal = add_animal("Jaws", owner = Angela, type = "Bunnies")
    print "add animal worked"
    print angelas_other_animal
    add_picture(animal = angelas_other_animal, caption = "he's an asshole", title = "Jaws the rabbit", picture = "images/Black_Rabbit_1.jpg")
    add_picture(animal = angelas_other_animal, caption = "he's cute though", title = "Jaws the rabbit", picture = "images/Black_Rabbit_2.jpg")
    add_picture(animal = angelas_other_animal, caption = "I love Jaws", title = "Jaws the rabbit", picture = "images/Black_Rabbit_3.jpg")

    Catherine = add_user("Catherine", "cathie@legit.com", "password", "www.ihavenofriends.com", "profile_images/Catherine.jpeg")
    print "add user worked"
    print Catherine
    catherines_animal = add_animal("Nancy", owner = Catherine, type = "Cats")
    print "add animal worked"
    print catherines_animal
    add_picture(animal = catherines_animal, caption = "This is my cat, Nancy", title = "Nancy the cat", picture = "images/White_Cat_1.jpg")
    add_picture(animal = catherines_animal, caption = "She's a little sweetie", title = "Nancy the cat", picture = "images/White_Cat_2.jpg")
    add_picture(animal = catherines_animal, caption = "Look at all the fluff", title = "Nancy the cat", picture = "images/White_Cat_3.jpg")

    Alan = add_user("Alan", "alan@legit.com", "password", "www.checkme.com", "profile_images/Alan.jpg")
    print "add user worked"
    print Alan
    alans_animal = add_animal("Megalodon", owner = Alan, type = "Dogs")
    print "add animal worked"
    print alans_animal
    add_picture(animal = alans_animal, caption = "This is my dog, Megalodon", title = "Megalodon the dog", picture = "images/Dog_1.jpg")
    add_picture(animal = alans_animal, caption = "He's a rather large dog", title = "Megalodon the dog", picture = "images/Dog_2.jpg")
    add_picture(animal = alans_animal, caption = "He could probably eat a child if he wanted", title = "Megalodon the dog", picture = "images/Dog_3.jpg")
    alans_other_animal = add_animal("Athena", owner = Alan, type = "Reptiles")
    print "add animal worked"
    print alans_other_animal
    add_picture(animal = alans_other_animal, caption = "This is my gecko, Athena", title = "Athena the gecko", picture = "images/Gecko_1.jpg")
    add_picture(animal = alans_other_animal, caption = "She's not particularly goddess like but whatever", title = "Athena the gecko", picture = "images/Gecko_2.jpg")
    add_picture(animal = alans_other_animal, caption = "She's a moody wee thing", title = "Athena the gecko", picture = "images/Gecko_3.jpg")

    Melissa = add_user("Melissa", "mel@legit.com", "password", "www.partyallnight.com", "profile_images/Melissa.jpg")
    print "add user worked"
    print Melissa
    melissas_animal = add_animal("Princess", owner = Melissa, type = "Bunnies")
    print "add animal worked"
    print melissas_animal
    add_picture(animal = melissas_animal, caption = "This is my bunny, Princess", title = "Princess the bunny", picture = "images/Rabbit_1.jpg")
    add_picture(animal = melissas_animal, caption = "She's my tiny baby", title = "Princess the bunny", picture = "images/Rabbit_2.jpg")
    add_picture(animal = melissas_animal, caption = "Princess understands me", title = "Princess the bunny", picture = "images/Rabbit_3.jpg")

    Vivian = add_user("Vivian", "vivian@legit.com", "password", "www.knittingpatterns.com", "profile_images/Vivian.jpg")
    print "add user worked"
    print Vivian
    vivians_animal = add_animal("Tweetie", owner = Vivian, type = "Birds")
    print "add animal worked"
    print vivians_animal
    add_picture(animal = vivians_animal, caption = "This is my canary, Tweetie", title = "Tweetie the canary", picture = "images/Canary_1.jpg")
    add_picture(animal = vivians_animal, caption = "Birds make me happy", title = "Tweetie the canary", picture = "images/Canary_2.jpg")
    add_picture(animal = vivians_animal, caption = "Tweetie doesn't interrupt my knitting", title = "Tweetie the canary", picture = "images/Canary_3.jpg")
    vivians_other_animal = add_animal("Barry", owner = Vivian, type = "Birds")
    print "add animal worked"
    print vivians_other_animal
    add_picture(animal = vivians_other_animal, caption = "This is my budgie, Barry", title = "Barry the budgie", picture = "images/Budgie_1.jpg")
    add_picture(animal = vivians_other_animal, caption = "Birds are my favourite", title = "Barry the budgie", picture = "images/Budgie_2.jpg")
    add_picture(animal = vivians_other_animal, caption = "Barry is quiet", title = "Barry the budgie", picture = "images/Budgie_3.jpg")

    Linda = add_user("Linda", "linda@legit.com", "password", "www.catsrgr8.com", "profile_images/Linda.jpg")
    print "add user worked"
    print Linda
    lindas_animal = add_animal("Tiger Lily", owner = Linda, type = "Cats")
    print "add animal worked"
    print lindas_animal
    add_picture(animal = lindas_animal, caption = "This is my cat, Tiger Lily", title = "Tiger Lily the cat", picture = "images/Tiggy_1.jpg")
    add_picture(animal = lindas_animal, caption = "She stays outside a lot", title = "Tiger Lily the cat", picture = "images/Tiggy_2.jpg")
    add_picture(animal = lindas_animal, caption = "I love my cat", title = "Tiger Lily the cat", picture = "images/Tiggy_3.jpg")

    Nathan = add_user("Nathan", "nathan@legit.com", "password", "www.nateisgreat.com", "profile_images/Nathan.jpg")
    print "add user worked"
    print Nathan
    nathans_animal = add_animal("Saffron", owner = Nathan, type = "Horses")
    print "add animal worked"
    print nathans_animal
    add_picture(animal = nathans_animal, caption = "This is my horse, Saffron", title = "Saffron the horse", picture = "images/Horse_1.jpg")
    add_picture(animal = nathans_animal, caption = "I love spending time with Saffron", title = "Saffron the horse", picture = "images/Horse_2.jpg")
    add_picture(animal = nathans_animal, caption = "Saffron makes me happy", title = "Saffron the horse", picture = "images/Horse_3.jpg")
    nathans_other_animal = add_animal("Melinda", owner = Nathan, type = "Fish")
    print "add animal worked"
    print nathans_other_animal
    add_picture(animal = nathans_other_animal, caption = "This is my fish, Melinda", title = "Melinda the fish", picture = "images/Black_Fish_1.jpg")
    add_picture(animal = nathans_other_animal, caption = "Fish are cool", title = "Melinda the fish", picture = "images/Black_Fish_2.jpg")
    add_picture(animal = nathans_other_animal, caption = "I hope she is happy", title = "Melinda the fish", picture = "images/Black_Fish_3.jpg")
    nathans_third_animal = add_animal("Bruce", owner = Nathan, type = "Others")
    print "add animal worked"
    print nathans_third_animal
    add_picture(animal = nathans_third_animal, caption = "This is my terrapin, Bruce", title = "Bruce the terrapin", picture = "images/Terrapin_1.jpg")
    add_picture(animal = nathans_third_animal, caption = "He likes water", title = "Bruce the terrapin", picture = "images/Terrapin_2.jpg")
    add_picture(animal = nathans_third_animal, caption = "He's only a little guy", title = "Bruce the terrapin", picture = "images/Terrapin_3.jpg")

    Will = add_user("Will", "will@legit.com", "password", "www.willwallace.com", "profile_images/Will.jpg")
    print "add user worked"
    print Will
    wills_animal = add_animal("Charlie", owner = Will, type = "Others")
    print "add animal worked"
    print wills_animal
    add_picture(animal = wills_animal, caption = "This is my chinchilla, Charlie", title = "Charlie the chinchilla", picture = "images/Chinchilla_1.jpg")
    add_picture(animal = wills_animal, caption = "He loves baths", title = "Charlie the chinchilla", picture = "images/Chinchilla_2.jpg")
    add_picture(animal = wills_animal, caption = "He is very energetic", title = "Charlie the chinchilla", picture = "images/Chinchilla_3.jpg")
    wills_other_animal = add_animal("Jasmine", owner = Will, type = "Fish")
    print "add animal worked"
    print wills_other_animal
    add_picture(animal = wills_other_animal, caption = "This is my fish, Jasmine", title = "Jasmine the fish", picture = "images/Fish_1.jpg")
    add_picture(animal = wills_other_animal, caption = "They're a very pretty fish", title = "Jasmine the fish", picture = "images/Fish_2.jpg")
    add_picture(animal = wills_other_animal, caption = "My fish is the best", title = "Jasmine the fish", picture = "images/Fish_3.jpg")

    Stacy = add_user("Stacy", "stacy@legit.com", "password", "www.stacyisme.com", "profile_images/Stacy.jpg")
    print "add user worked"
    print Stacy
    stacys_animal = add_animal("Frodo", owner = Stacy, type = "Horses")
    print "add animal worked"
    print stacys_animal
    add_picture(animal = stacys_animal, caption = "This is my horse, Frodo", title = "Frodo the horse", picture = "images/Grey_Horse_1.jpg")
    add_picture(animal = stacys_animal, caption = "Frodo is a lovely horse", title = "Frodo the horse", picture = "images/Grey_Horse_2.jpg")
    add_picture(animal = stacys_animal, caption = "Frodo loves apples", title = "Frodo the horse", picture = "images/Grey_Horse_3.jpg")
    stacys_other_animal = add_animal("Martha", owner = Stacy, type = "Others")
    print "add animal worked"
    print stacys_other_animal
    add_picture(animal = stacys_other_animal, caption = "This is my hamster, Martha", title = "Martha the hamster", picture = "images/Hamster_1.jpg")
    add_picture(animal = stacys_other_animal, caption = "She's a greedy little ham", title = "Martha the hamster", picture = "images/Hamster_2.jpg")
    add_picture(animal = stacys_other_animal, caption = "She likes to go on her wheel late at night", title = "Martha the hamster", picture = "images/Hamster_3.jpg")

    Ben = add_user("Ben", "ben@legit.com", "password", "www.bigben.com", "profile_images/Ben.jpg")
    print "add user worked"
    print Ben
    bens_animal = add_animal("Bailey", owner = Ben, type = "Bunnies")
    print "add animal worked"
    print bens_animal
    add_picture(animal = bens_animal, caption = "This is my rabbit, Bailey", title = "Bailey the rabbit", picture = "images/Bunny_1.jpg")
    add_picture(animal = bens_animal, caption = "Got him after my wife died", title = "Bailey the rabbit", picture = "images/Bunny_2.jpg")
    add_picture(animal = bens_animal, caption = "He likes lettuce", title = "Bailey the rabbit", picture = "images/Bunny_3.jpg")

    Margaret = add_user("Margaret", "margo@legit.com", "password", "www.bigmags.com", "profile_images/Margaret.jpg")
    print "add user worked"
    print Margaret
    margarets_animal = add_animal("Goldie", owner = Margaret, type = "Dogs")
    print "add animal worked"
    print margarets_animal
    add_picture(animal = margarets_animal, caption = "This is my dog, Goldie", title = "Goldie the dog", picture = "images/Labrador_1.jpg")
    add_picture(animal = margarets_animal, caption = "Goldie loves walks", title = "Goldie the dog", picture = "images/Labrador_2.jpg")
    add_picture(animal = margarets_animal, caption = "Goldie loves her dinner", title = "Goldie the dog", picture = "images/Labrador_3.jpg")
    margarets_other_animal = add_animal("Shadow", owner = Margaret, type = "Cats")
    print "add animal worked"
    print margarets_other_animal
    add_picture(animal = margarets_other_animal, caption = "This is my cat, Shadow", title = "Shadow the cat", picture = "images/Cat_1.jpg")
    add_picture(animal = margarets_other_animal, caption = "Shadow doesn't like outdoors", title = "Shadow the cat", picture = "images/Cat_2.jpg")
    add_picture(animal = margarets_other_animal, caption = "He also likes sleep", title = "Shadow the cat", picture = "images/Cat_3.jpg")

def add_picture(animal, caption, title, picture, views=0, likes=0):
    p = Picture.objects.get_or_create(user = animal, caption = caption, title=title, likes=likes, views=views, picture = picture)
    return p

def add_animal(name, owner, type,  views = 0, likes = 0):
    a = AnimalProfile.objects.get_or_create(name = name, owner = owner, animalType = type)[0]
    return a
    
#picture should be defined as a directory inside the media folder, so you will have to copy them manually for now :(
def add_user(username, email, password, website, picture):
    user =  django.contrib.auth.models.User(username = username, email=email, password = password)
    user.set_password(password)
    user.save()
    uprofile = UserProfile(user = user, website = website, picture = picture)
    uprofile.save()
    return uprofile

if __name__ == '__main__':
    print "Starting pawcrastination population script..."
    populate()

    
