import random, time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        return result, f'{elapsed:.6f}'
    return wrapper

@timer
def minimum_shelves(book_sizes, shelf_width=1000):
    sorted_books = sorted(book_sizes, reverse=True)
    shelves = []

    for book in sorted_books:
        placed = False

        for i in range(len(shelves)):
            if shelves[i] >= book:
                shelves[i] -= book
                placed = True
                break
            
        if not placed:
            shelves.append(shelf_width - book)

    return len(shelves)

def main(*args):
    result = []
    
    for arg in args:
        books = [random.randint(10,50) for i in range(arg)]

        result.append(minimum_shelves(books)[1])
        
    print(result)
    return result