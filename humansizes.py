# Book 1 Chapter 2 Python


#this is a diccionary of lists
SUFFIXES = {
    1000: ['KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'],
    1024: ['KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB']
    }

#function = you use def and ends with a :
#this function below has parameters

def approximate_size(size, a_kilobyte_is_1024_bytes=True):

#this is a docstring in python - gives info to others - function documentation after the function
    '''Convert a file size to human-readable form.

    (this is a docstring)

    Keyword arguments:
    size -- file size in bytes
    a_kilobyte_is_1024_bytes -- if True (default), use multiples of 1024
                                if False, use multiples of 1000

    Returns: string

    '''
    if size < 0:
        raise ValueError('number must be non-negative')

#ternary in JS one line if else
    multiple = 1024 if a_kilobyte_is_1024_bytes else 1000

#for loop -
    for suffix in SUFFIXES[multiple]:
        size /= multiple  #same as size/multiple
        if size < multiple:
            return '{0:.1f} {1}'.format(size, suffix)

    raise ValueError('number too large')

if __name__ == '__main__':
print(approximate_size(16384, False))
    print(approximate_size(size=16384, a_kilobyte_is_1024_bytes=False))
    print(approximate_size(-16384))