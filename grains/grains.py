def on_square(square):
    return 2**(square-1)

def total_after(square):
    return sum(2**i for i in range(0, square))
