from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from models import *
from collections import Counter

# The index function is called when root is visited
def index(request):
    return render(request, 'belt_reviewer_app/index.html')


def set_session(request, user):
    request.session['id'] = user.id
    request.session['user_name'] = user.name
    request.session['logged_in'] = True
    request.session['poke_counter'] = 0

def get_users():
    # Modify this function to get more items from the DB if needed.
    users = User.objects.all()

    return users

def dashboard(request):
    # If we are here, we are logged in!
    latest_three_reviews_details = []
    all_book_reviews = []
    all_users = get_users()
    for book_id in Review.objects.all().values_list('book_id', flat=True).distinct():
        all_book_reviews.append(
            {
                "book_title": Book.objects.get(id=book_id).name,
                "book_title_id": book_id,
            }
        )

    for r in Review.objects.order_by("-created_at")[:3]:
        latest_three_reviews_details.append(
            {
                "reviewer_id": r.reviewer_id,
                "reviewer": User.objects.get(id=r.reviewer_id).name,
                "book_title": Book.objects.get(id=r.book_id).name,
                "book_rating": Book.objects.get(id=r.book_id).rating,
                "book_title_id": r.book_id,
                "review_content": r.content,
                "review_date_posted": r.created_at

            }
        )

    context = {
        "latest_three_reviews_list": latest_three_reviews_details,
        "all_book_reviews": all_book_reviews
    }

    return render(request, "belt_reviewer_app/initium.html", context)

def login(request):
    notifications, user = User.objects.validate_login(request.POST)

    if notifications:
        for error in notifications:
            messages.error(request, error['message'], error['message_tag'])
            return redirect('/')
    if user:
        set_session(request, user)
        return redirect('/dashboard')

def registration(request):
    errors, valid_entry = User.objects.validate_registration(request.POST)

    if valid_entry:
        # The new user records has been validated.  Let's add the user!
        user = User.objects.new_user(request.POST)
        set_session(request, user)
        return redirect('/dashboard')
    else:
        for entry in errors:
            messages.error(request, entry['message'], entry['message_tag'])
            return redirect('/')


def signout(request):
    request.session.clear()
    return redirect('/')

def get_review_details(request, id):
    reviews_details = []

    for r in Review.objects.filter(book_id=id):
        reviews_details.append(
            {
                "reviewer_id": r.reviewer_id,
                "reviewer": User.objects.get(id=r.reviewer_id).name,
                "book_title": Book.objects.get(id=r.book_id).name,
                "book_title_id": r.book_id,
                "review_content": r.content,
                "review_date_posted": r.created_at,
                "review_id": r.id

            }
        )

    return reviews_details


def create_rating_menu():
    ratings = []

    for rate in range(1, 6):
        ratings.append(rate)

    print "IN create_rating_menu: {}".format(ratings)
    return ratings


def show_book_review(request, id):
    """
        Shows details about the book and related reviews.
    """
    context = {
        "all_reviews": get_review_details(request, id),
        "book_title": Book.objects.get(id=id).name,
        "book_rating": Book.objects.get(id=Review.objects.get(id=8).book_id).rating,
        "book_author": Author.objects.get(id=Book.objects.get(id=id).author_id).name,
        "book_ratings": create_rating_menu()
    }

    return render(request, "belt_reviewer_app/show_book.html", context)

def delete_review(request, id):
    """
        Deletes reviews associated with a given user.
    """
    review = Review.objects.get(id=id)
    book_id = review.book_id
    review.delete()

    return redirect('/books/{}'.format(book_id))


def add_book_review(request):
    """
       Renders the page to add a book review.
    """
    authors = Author.objects.all()


    context = {
        'authors_list': authors,
        'book_ratings': create_rating_menu()
    }
    # Renders a template that shows information for the user.
    return render(request, "belt_reviewer_app/add_book.html", context)


def book_found(title):

    try:
        book = Book.objects.get(name=title)
    except Exception:
        book = None

    return book



def add(request):
    """
        Makes the request to the backend to add the new book review.
    """

    review_content = request.POST['review_content']
    uploader = User.objects.get(id=request.session['id'])

    title = request.POST['book_title']
    # Check if the book is already stored in the DB.
    book = book_found(title)

    try:
        # See if the author is already present.
        author = Author.objects.get(name=request.POST['author_value'])
    except:
        # If not found, then create it!
        author = Author.objects.create(name=request.POST['author_value'])

    if book:
        # Add a review to the existing book
        b = Book.objects.get(id=book.id)
        Review.objects.create(content=review_content, book=b, reviewer=uploader)
    else:
        # Add a new book and a review
        book = Book.objects.create(name=title, author=author, uploader=uploader)
        Review.objects.create(content=review_content, book=book, reviewer=uploader)

    return redirect('/books/{}'.format(book.id))



def show_user(request, id):
    """
        Shows details about a user/reviewer.
    """
    user = User.objects.get(id=id)
    all_books_reviewed_by_user = []
    seen = []

    for r in Review.objects.filter(reviewer_id=id):
        Book.objects.get(id=r.book_id)
        if Book.objects.get(id=r.book_id).name not in seen:
            seen.append(Book.objects.get(id=r.book_id).name)
            all_books_reviewed_by_user.append(
                {
                    "book_name": Book.objects.get(id=r.book_id).name,
                    "book_id": r.book_id
                }
            )
        else:
            pass

    context = {
        "user_name": user.name,
        "user_birthday": user.birth_date,
        "user_email": user.email,
        "book_review_count": user.book_reviews.count(),
        "book_review_list": all_books_reviewed_by_user
    }

    # Renders a template that shows information for the user.
    return render(request, "belt_reviewer_app/show_user.html", context)




