import string
from .models import Bitly

def code_gen():
    import random
    shrtcd = ''
    chars =string.ascii_lowercase+string.ascii_uppercase+string.digits
    for i in range(6):
        shrtcd+=random.choice(chars)
    return shrtcd

def create_shortcode():
    shrtcd=code_gen()
    qs= Bitly.objects.filter(Shortcode__iexact=shrtcd)
    if qs.exists():
        return create_shortcode()
    return shrtcd