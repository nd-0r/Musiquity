from backend.search import search

if __name__ == '__main__':
  q = input('Enter a query: ')
  print(search(q))