if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv

def module():
    return Johanna

class Johanna(adv.Adv):
    pass

if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1 
        `s2 
        `s3
        `fs,seq=5
        """
    adv_test.test(module(), conf, verbose=0)

