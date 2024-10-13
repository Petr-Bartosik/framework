from django.shortcuts import render

def main(request):
    return render(request, 'core/main.html')

def writers(request):
    return render(request, 'core/writers.html')
def writers(request):

    authors = ['Hemingway', 'Shakespeare']
    return render(request, 'core/writers.html', {'authors': authors})
def books(request):
    return render(request, 'core/books.html')


from django.shortcuts import render, redirect

def author_detail(request, author_name):
    authors = {
        'Hemingway': 'Informace o Ernestu Hemingwayovi...',
        'Shakespeare': """William Shakespeare (pokřtěn 26. dubna 1564, Stratford nad Avonou – 3. května 1616 podle gregoriánského kalendáře, Stratford nad Avonou) byl anglický básník, dramatik a herec, který bývá považován za největšího anglicky píšícího spisovatele a celosvětově nejvýznamnějšího dramatika. 
        Je často nazýván anglickým národním básníkem a „bardem z Avonu“. Připisuje se mu přibližně 38 dochovaných her, 154 sonetů, dvě dlouhé epické básně a několik dalších básní. 
        Jeho hry byly přeloženy do všech hlavních živých jazyků a jsou uváděny častěji než hry jakéhokoli jiného dramatika..."""
    }

    if author_name in authors:
        context = {'author_info': authors[author_name]}
        return render(request, 'core/author_detail.html', context)
    else:
        return render(request, 'core/404.html')


from django.shortcuts import render, redirect

def book_detail(request, book_id):
    books = {
        1: 'Kniha na prvním místě:  "1984" od George Orwella',
        2: 'Kniha na druhém místě:  "Pýcha a předsudek" od Jane Austen',
        3: 'Kniha na třetím místě:  "Moby Dick" od Hermana Melvilla',
    }


    if book_id in books:
        context = {'book_id': book_id, 'book_info': books[book_id]}
        return render(request, 'core/book_detail.html', context)
    else:

        return redirect('books')


def book_info(request, book_id):
    books = {
        1: 'Kniha na prvním místě: "1984" od George Orwella',
        2: 'Kniha na druhém místě: "Pýcha a předsudek" od Jane Austen',
        3: 'Kniha na třetím místě: "Moby Dick" od Hermana Melvilla',
    }


    if book_id in books:
        context = {'book_id': book_id, 'book_info': books[book_id]}
        return render(request, 'core/book_detail.html', context)
    else:
        return redirect('books')

def book_info(request, author_name, book_title):
    books = {
        'Hemingway': {
            'The_Old_Man_and_the_Sea': 'Informace o knize "The Old Man and the Sea".',
            'The_Sun_Also_Rise': 'Informace o knize "The Sun Also Rises".',
        }
    }

    if author_name in books and book_title in books[author_name]:
        book_info = books[author_name][book_title]
        context = {'book_info': book_info, 'author_name': author_name}
        return render(request, 'core/book_info.html', context)
    else:
        return redirect('author_detail', author_name=author_name)


def writers_info(request):
    author = request.GET.get('writers')
    year = request.GET.get('year')

    books = {
        'Hemingway': {
            1926: 'Informace o knihách napsaných Hemingwaye v roce 1926.',
            1940: 'Informace o knihách napsaných Hemingwaye v roce 1940.',
        }
    }

    if author in books and int(year) in books[author]:
        book_info = books[author][int(year)]
        context = {'book_info': book_info}
        return render(request, 'core/writers_info.html', context)
    else:
        return redirect('author_detail', author_name=author)






from django.shortcuts import render, redirect

def citizen_info(request):
    author = request.GET.get('writers')
    year = request.GET.get('year')

    books = {
        'Hemingway': {
            1926: 'Informace o knihách napsaných Hemingwaye v roce 1926.',
            1940: 'Informace o knihách napsaných Hemingwaye v roce 1940.',
        }
    }

    if author in books and int(year) in books[author]:
        book_info = books[author][int(year)]
        context = {'citizen_info': book_info}
        return render(request, 'core/citizen_info.html', context)
    else:
        return redirect('author_detail', author_name=author)

