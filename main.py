import os, sys
import dns.resolver
from threading import Thread

def get_ip(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            return str(rdata)

    except:
        return None

def mass_check_ip(filename, pre_ip):
    f = open(filename).read().splitlines()
    g = []

    div = int(len(f)/10)

    class check_1(Thread):
        def run(self):

            ndiv = div
            for i in range(0, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_2(Thread):
        def run(self):

            ndiv = (div*2)
            for i in range(div, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_3(Thread):
        def run(self):

            ndiv = (div*3)
            for i in range(div*2, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_4(Thread):
        def run(self):

            ndiv = div*4
            for i in range(div*3, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_5(Thread):
        def run(self):

            ndiv = div*5
            for i in range(div*4, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_6(Thread):
        def run(self):

            ndiv = div*6
            for i in range(div*5, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_7(Thread):
        def run(self):

            ndiv = div*7
            for i in range(div*6, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_8(Thread):
        def run(self):

            ndiv = div*8
            for i in range(div*7, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_9(Thread):
        def run(self):

            ndiv = div*9
            for i in range(div*8, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    class check_10(Thread):
        def run(self):

            ndiv = div*10
            for i in range(div*9, ndiv):

                domain = f[i]
                req = get_ip(domain)
                i += 1

                print(i)
                try:
                    if pre_ip in req:
                        print(domain)
                        with open(f'new_domain_{pre_ip}.dat', 'a+') as fp:
                            fp.write(domain + '\n')
                except:
                    continue

    t = check_1()
    t_ = check_2()
    t__ = check_3()
    t___ = check_4()
    t____ = check_5()
    t_____ = check_6()
    t_______ = check_7()
    t________ = check_8()
    t_________ = check_9()
    t__________ = check_10()

    t.start()
    t_.start()
    t__.start()
    t___.start()
    t____.start()
    t_____.start()
    t_______.start()
    t________.start()
    t_________.start()
    t__________.start()

    t.join()
    t_.join()
    t__.join()
    t___.join()
    t____.join()
    t_____.join()
    t_______.join()
    t________.join()
    t_________.join()
    t__________.join()

if __name__=="__main__":
    filename=sys.argv[1]
    pre_ip = sys.argv[2]
    
    mass_check_ip (filename, pre_ip)