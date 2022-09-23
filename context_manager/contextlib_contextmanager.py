import contextlib

@contextlib.contextmanager
def make_context():
    print('entering')
    try:
        yield {}
    except RuntimeError as err:
        print('ERROR', err)
    finally:
        print('exiting')

print('Normal:')
with make_context() as value:
    print('inside with statement:', value)

print('\nhandled error:')
with make_context() as value:
    raise RuntimeError('showing example of handling a error')

print('\nUnhandled error:')
with make_context() as value:
    raise ValueError('this exception is not handled')
