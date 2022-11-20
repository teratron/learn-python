# pip install beautifulsoup4
# и
# pip install google

try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

# to search
query = "Python"  # Задаем текст для поиск в гугле

for j in search(query, tld="co.in", num=10, stop=10, pause=2):
    print(j)
