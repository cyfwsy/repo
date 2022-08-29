import gc
# from pprint import pprint
import weakref

gc.set_debug(gc.DEBUG_UNCOLLECTABLE)


class ExpensiveObject:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'ExpensiveObject({})'.format(self.name)

    def __del__(self):
        print('   (Deleting<{}>)'.format(self))


def demo(cache_factory):
    # Hold object so any weak references are not removed immediately
    all_refs = {}
    # Create the cathe using factory
    cache = cache_factory()
    for name in ['one', 'two', 'three']:
        o = ExpensiveObject(name)
        cache[name] = o
        all_refs[name] = o
        del o  # decrese reference

    print('all_refs =', end='')
    print(all_refs)
    print('\n Before cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print('  {} = {}'.format(name, value))
        del value  # decrese ref

    # Remove all reference to the object except the cache
    print('\n Cleanup')
    del all_refs
    gc.collect()
    print('\n After cache contains:', list(cache.keys()))
    for name, value in cache.items():
        print(' {} = {}'.format(name, value))

    print('demo returning')
    return


if __name__ == '__main__':
    demo(dict)
    print('------------------------------------------------')
    demo(weakref.WeakValueDictionary)
