from django.shortcuts import render, redirect , HttpResponse
from log_reg_app.models import *
from .models import *

# MULTIPLE APPS HAVE ISSUES WITH SIMILAR FILE NAMES SEPERATE WITH FOLDERS
# CARRYING USER FROM REQUEST SESSION
def dashboard(request):
    # if check checks if there is a user logged in, if not it redirects
    if 'user_id' not in request.session:
        return redirect ('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'post': Post.objects.all(),
    }
    return render (request, 'dashboard/index.html', context)
 
def delete(request, post_id):
    # Deleting a post with the information of the current logged in user 
    to_delete = Post.objects.get(id=post_id)
    if to_delete.author_id == request.session['user_id']:
        to_delete.delete()
    return redirect('/posts')

def post_mess(request):
    Post.objects.create(title=request.POST['title'],content=request.POST['content'], author=User.objects.get(id=request.session['user_id']))
    return redirect('/posts')




def post_comment(request, id):
    # AUTHOR THAT IS POSTING COMMENT 
    author = User.objects.get(id=request.session['user_id'])
    # ON WHAT MESSAGE 
    message = Post.objects.get(id=id)
    # CREATING THE COMMENT
    Comment.objects.create(comment=request.POST['comment'], author=author, message_post=message)
    return redirect('/posts')

def delete_comment(request, id):
    destroyed = Comment.objects.get(id=id)
    destroyed.delete()
    return redirect('/posts')