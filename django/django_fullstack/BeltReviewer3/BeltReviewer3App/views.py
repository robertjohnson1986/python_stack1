from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, UserManager, Reviews, Author, Books
import bcrypt

# Create your views here.


def index(request):
    request.session.flush()
    return render(request, 'index.html')


def register(request):  # post redirect
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        # hash the password
        hashed_pw = bcrypt.hashpw(
            request.POST['password'].encode(), bcrypt.gensalt()).decode()
        # create a user
        new_user = User.objects.create(
            first_name=request.POST['first_name'], last_name=request.POST[
                'last_name'], email=request.POST['email'], password=hashed_pw
        )
        # create a session
        request.session['user_id'] = new_user.id
        return redirect('/success')
    return redirect('/')


# # render the success page


def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    this_user = User.objects.filter(id=request.session['user_id'])
    context = {
        'user': this_user[0],
        'my_reviews' : Reviews.objects.filter(reviewer=this_user[0]),
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_authors' : Author.objects.all()
    }

    return render(request, 'success.html', context)

def post_review(request):
    print(request.POST['review'])
    errors = Reviews.objects.message_validator(request.POST)

    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/success')
    else:
        user = User.objects.get(id=request.session["user_id"])
        if len(request.POST['custom_author']) <0:
            author = Author.objects.get(id=request.POST['author'])
        else:
            author = Author.objects.create(name=request.POST['custom_author'])
        review = Reviews.objects.create(
            review = request.POST['review'],
            rating = request.POST['rating'],
            book_reviewed = Books.objects.create(author= author, title=request.POST['title']),
            reviewer = user
        )
        

        return redirect('/success')

# def post_description(request):
#     if request.method == 'POST':
#         errors = Books.objects.message_validator(request.POST)
#         if len(errors) > 0:
#             for key, value in errors.items():
#                 messages.error(request, value)
#         else:
#             Books.objects.create(description=request.POST['description'])

# def like(request, id):
#     user = User.objects.get(id=request.session["user_id"])
#     book = Books.objects.get(id=id)
#     user.liked_books.add(book)
#     messages.success(request, "Like Registered")
#     return redirect('/success')

# def unlike(request, id):
#     user = User.objects.get(id=request.session["user_id"])
#     book = Books.objects.get(id=id)
#     user.liked_books.remove(book)
#     messages.success(request, "Like Removed")
#     return redirect('/success')

# log in

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) != 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
        this_user = User.objects.filter(email=request.POST['email'])
        request.session['user_id'] = this_user[0].id
        return redirect('/success')
    return redirect('/')
# # log out

# def book_page(request, id):
#     context = {
#         'one_book' : Books.objects.get(id=id)
#     }
#     return render(request, 'book_page.html', context)

# def update(request, id):
#     errors = Books.objects.message_validator(request.POST)

#     if len(errors):
#         for key, value in errors.items():
#             messages.error(request, value)
#         return redirect(f'/book_page/{id}')
#     else:
#         book = Books.objects.get(id=id)
#         book.message = request.POST['message']
#         book.description = request.POST['description']
#         book.save()

#     return redirect(f'/book_page/{id}')

# def delete_comment(request, id):
#     destroyed = Comment.objects.get(id=id)
#     destroyed.delete()
#     return redirect('/success')

# def delete_message(request, id):
#     destroyed = Books.objects.get(id=id)
#     destroyed.delete()
#     return redirect('/success')

def logout(request):
    request.session.flush()
    return redirect('/')


