# škare, papir, kamen, gušter, Spock

igrac1 = input('Unesi š, p, k, g ili s: ')
igrac2 = input('Unesi š, p, k, g ili s: ')

if igrac1 == 'š' and igrac2 == 'š':
    print('Neriješeno je!')
elif igrac1 == 'š' and igrac2 == 'p':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'š' and igrac2 == 'k':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'š' and igrac2 == 'g':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'š' and igrac2 == 's':
    print('Pobijedio je igrač 2!')

if igrac1 == 'p' and igrac2 == 'š':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'p' and igrac2 == 'p':
    print('Neriješeno je!')
elif igrac1 == 'p' and igrac2 == 'k':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'p' and igrac2 == 'g':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'p' and igrac2 == 's':
    print('Pobijedio je igrač 1!')

if igrac1 == 'k' and igrac2 == 'š':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'k' and igrac2 == 'p':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'k' and igrac2 == 'k':
    print('Neriješeno je!')
elif igrac1 == 'k' and igrac2 == 'g':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'k' and igrac2 == 's':
    print('Pobijedio je igrač 2!')

if igrac1 == 'g' and igrac2 == 'š':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'g' and igrac2 == 'p':
    print('Pobijedio je igrač 1!')
elif igrac1 == 'g' and igrac2 == 'k':
    print('Pobijedio je igrač 2!')
elif igrac1 == 'g' and igrac2 == 'g':
    print('Neriješeno je!')
elif igrac1 == 'g' and igrac2 == 's':
    print('Pobijedio je igrač 1!')

if igrac1 == 's' and igrac2 == 'š':
    print('Pobijedio je igrač 1!')
elif igrac1 == 's' and igrac2 == 'p':
    print('Pobijedio je igrač 2!')
elif igrac1 == 's' and igrac2 == 'k':
    print('Pobijedio je igrač 1!')
elif igrac1 == 's' and igrac2 == 'g':
    print('Pobijedio je igrač 2!')
elif igrac1 == 's' and igrac2 == 's':
    print('Neriješeno je!')