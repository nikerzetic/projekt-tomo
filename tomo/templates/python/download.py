{% load my_tags %}#####################################################################@@#
# {{ problem.title }} {% if problem.description %}
#
# {{ problem.description|remove_markdown|safe }}{% endif %}
#####################################################################@@#

{{ problem.preamble|safe }}

{% for part in parts %}
################################################################@{{ part.id|stringformat:'06d'}}#
# {{ forloop.counter }}) {{ part.description|remove_markdown|safe }}
################################################################{{ part.id|stringformat:'06d'}}@#
{% with attempts|get:part.id as attempt %}{% if attempt.solution %}{{ attempt.solution|safe }}{% endif %}{% endwith %}

{% endfor %}








































































































#####################################################################@@#
# Kode pod to črto nikakor ne spreminjajte.
########################################################################

"TA VRSTICA JE PRAVILNA."
"ČE VAM PYTHON SPOROČI, DA JE V NJEJ NAPAKA, SE MOTI."
"NAPAKA JE NAJVERJETNEJE V ZADNJI VRSTICI VAŠE KODE."
"ČE JE NE NAJDETE, VPRAŠAJTE ASISTENTA."



























































import json, os, re, sys, shutil
from urllib.error import HTTPError
from urllib.parse import urlencode
from urllib.request import urlopen
{% include 'python/check.py' %}

def _check():
    _filename = os.path.abspath(sys.argv[0])
    with open(_filename, encoding='utf-8') as _f:
        _source = _f.read()

    Check.initialize([
        {
            'part': int(match.group('part')),
            'solution': match.group('solution').strip()
        } for match in re.compile(
            r'^#+@(?P<part>\d+)#\n' # beginning of header
            r'(^# [^\n]*\n)*'       # description
            r'#+\1@#\n'             # end of header
            r'(?P<solution>.*?)',   # solution
            r'^(# )?(?=#+@)',       # beginning of next part
            flags=re.DOTALL|re.MULTILINE
        ).finditer(_source)
    ])

    {% for part in parts %}
    if Check.part():
        {{ part.validation|indent:"        "|safe }}
    {% endfor %}

    Check.summarize()
    {% if authenticated %}
    print('Shranjujem rešitve na strežnik...')
    post = urlencode({
        'data': '{{ data|safe }}',
        'timestamp' : '{{ timestamp }}',
        'signature': '{{ signature }}',
        'attempts': Check.dump(),
        'source': _source,
    }).encode('utf-8')
    try:
        r = urlopen('http://{{ request.META.SERVER_NAME }}:{{ request.META.SERVER_PORT }}{% url upload %}', post)
        response = json.loads(r.read().decode('utf-8'))
        for (k, e) in response['judgments']:
            if e is None: print ("Podnaloga {0} je shranjena in sprejeta kot pravilna.".format(k))
            else: print ("Podnaloga {0} je shranjena in zavrnjena kot nepravilna ({1}).".format(k,e))
        if 'message' in response: print (response['message'])
    except HTTPError:
        print('Pri shranjevanju je prišlo do napake. Poskusite znova.')
    {% else %}
    print('Rešujete kot anonimni uporabnik, zato rešitve niso shranjene.')
    {% endif %}

_check()

#####################################################################@@#
