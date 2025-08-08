book_reviews = {"""
    '1':People tell you the world looks a certain way.
    Parents tell you how to think. Schools tell you how to think.
    TV. Religion. And then at a certain point,
    if you’re lucky, you realize you can make up your own mind.
    Nobody sets the rules but you. You can design your own life."""
}
book=input('Enter the name of the book:')

found=False
for tittle in book_reviews:
    if tittle in book:
        print(book_reviews[tittle])
        found=True
        break
    if not found:
        print("You have not read the book yet, but you could be the first to review it !")