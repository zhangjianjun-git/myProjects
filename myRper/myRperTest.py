import reprlib

reprlib_repr = reprlib.repr(set('supercalifragilisticexpialidocious'))
print(reprlib_repr)
"set(['a', 'c', 'd', 'e', 'f', 'g', ...])"

urls_str = '/http://www.cwi.nl:80/%7Eguido/'
urls = urls_str.lstrip('/')
print(urls)
