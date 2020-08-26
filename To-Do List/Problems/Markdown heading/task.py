def heading(sentences, hashtags=1):
    return min(max(hashtags, 1), 6) * '#' + ' ' + sentences
