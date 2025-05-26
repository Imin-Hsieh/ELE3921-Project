from django.shortcuts import render
from django.views.decorators.http import require_GET
from post.models import Post
import re

# stop words retrieved from https://gist.github.com/sebleier/554280
STOP_WORDS = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

@require_GET
def search(request):
    q = request.GET.get("q", "")
    search_results = set() # set to avoid duplicates

    if q:
        terms = re.split(r"[ ,!'?.:;]", q) # split on and remove any of these characters
        for term in terms:
            if term.lower() not in STOP_WORDS:
                query_results = Post.objects.filter(content__icontains=term)
                search_results.update(query_results)

    context = {
        "title"  : "Search results",
        "posts" : list(search_results)
    }
    print(search_results)
    return render(request, "search/search_page.html", context=context)