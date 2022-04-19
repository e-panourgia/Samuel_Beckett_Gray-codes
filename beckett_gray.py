# import libraries
import argparse
import itertools

def is_cyclic(code):
    c = code[0] ^ code[-1]
    return not c & (c - 1)

def get_delta_sequence(code):
    is_cycle = is_cyclic(code)  # determine if code is cyclic
    delta = []
    for i in range(len(code)):

        # get next index
        if i == len(code) - 1:
            if not is_cycle:
                break
            i_next = 0
        else:
            i_next = i + 1

        delta.append(bin(code[i] ^ code[i_next])[2::][::-1].find('1'))
    return delta


def build_delta_sequences(codes):
    return [''.join(map(str, get_delta_sequence(code))) for code in codes]

def find_isomorphisms(delta_sequences, n):
    mappings = list(map(list, itertools.permutations(range(n))))    # generate all possible mappings
    all_groups = {}
    for mapping in mappings:
        grouped_sequences = {}
        for i, seq in enumerate(delta_sequences):
            mapped = ''.join(map(str, [mapping[int(c)] for c in seq])) 
            if mapped not in grouped_sequences:
                grouped_sequences[mapped] = []
            grouped_sequences[mapped].append(i)

        for i, seq in enumerate(delta_sequences):
            rev = seq[::-1]
            if rev in grouped_sequences:
                grouped_sequences[rev].append(i)

        for val in grouped_sequences.values():
            for i, v in enumerate(val):
                v_add = val[:i] + val[i+1:]
                if v not in all_groups:
                    all_groups[v] = set()
                all_groups[v] |= set(v_add)

    return all_groups

# change the price of bit index_i in x.
# -x, the current node in the hypercube
def Flip(x, index_i):
    return x ^ (2 ** index_i)


# to find all codes Gray !
def GC_DFS(d, x, max_coord, n, gc, visited, all_codes, cycles):
    """
    Input :
        -d, the recursion depth
        -x, the current node in the hypercube
        -max_coord, the maximum coordinate to be set in 𝑥
        -n, the number of bits of the Gray code
        -gc, a stack
    Data : 
        - visited, an boolean array of size 2 ^ n
        - all_codes, a list
    Result : 
        -  all_codes, contains all the Gray codes 
        that could be found
    """
    # Body of the algo 
    if d == 2 ** n:  # Condition of stopping the recursion
        code = gc.copy()
        all_codes.append(code)
        cycles.append(is_cyclic(code))
        return

    min_var = min(n - 1, max_coord)
    for index_i in range(min_var + 1):
        x = Flip(x, index_i)
        if visited[x] == False:
            visited[x] = True
            gc.append(x)
            GC_DFS(d + 1, x, max(index_i + 1, max_coord), n, gc, visited, all_codes, cycles)
            visited[x] = False
            gc.pop()
        x = Flip(x, index_i)


def BGC_DFS(d, x, max_coord, n, gc, queue, visited, beckett_gray_codes, cycles):
    """
    Input :
        -d, the recursion depth
        -x, the current node in the hypercube
        -max_coord, the maximum coordinate to be set in 𝑥
        -n, the number of bits of the Gray code
        -gc, a stack
    Data : 
        - visited, an boolean array of size 2 ^ n
        - all_codes, a list
    Result : 
        -  all_codes, contains all the Gray codes 
        that could be found
    """
    # Body of the algo
    if d == 2 ** n:  # Condition of stopping the recursion
        code = gc.copy()
        beckett_gray_codes.append(code)
        cycles.append(is_cyclic(code))
        return


    min_var = min(n - 1, max_coord)
    for index_i in range(min_var + 1):
        tmp_queue = queue.copy()
        x_index_i = 1 if x & 2 ** index_i else 0    # get i-th bit
        x = Flip(x, index_i)

        # If we change a 0 to 1 push to queue
        bg_visit_flag = True
        if x_index_i == 0:
            tmp_queue.append(index_i)
        else:  # else check Beckett Gray criterion
            if tmp_queue[0] != index_i:
                bg_visit_flag = False
            else:
                tmp_queue.pop(0)

        if visited[x] == False and bg_visit_flag:
            visited[x] = True
            gc.append(x)
            BGC_DFS(d + 1, x, max(index_i + 1, max_coord), n, gc, tmp_queue, visited, beckett_gray_codes, cycles)
            visited[x] = False
            gc.pop()
        x = Flip(x, index_i)


# Fix parametres 
parser = argparse.ArgumentParser(description='Beckett and Code_Gray')
parser.add_argument('-a', action="store_true")
parser.add_argument('-b', action="store_true")
parser.add_argument('-u', action="store_true")
parser.add_argument('-c', action="store_true")
parser.add_argument('-p', action="store_true")
parser.add_argument('-r', action="store_true")
parser.add_argument('-f', action="store_true")
parser.add_argument('-m', action="store_true")
parser.add_argument("number_of_bits", help="user gives the number of bits (positive integer)",
                    type=int)
args = parser.parse_args()
n = vars(args)
n = n.get('number_of_bits')


all_codes = []
cycles_all_codes = []

beckett_gray_codes = []
cycles_beckett_gray_codes = []

if args.a or args.c or args.p:
    gc = [0]  # stack
    visited = [False] * 2**n
    visited[0] = True
    GC_DFS(1, gc[0], 0, n, gc, visited, all_codes, cycles_all_codes)

if args.b or args.u:
    gc = [0]  # stack
    visited = [False] * 2 ** n
    visited[0] = True
    queue = []
    BGC_DFS(1, gc[0], 0, n, gc, queue, visited, beckett_gray_codes, cycles_beckett_gray_codes)

if args.a:
    for i, code in enumerate(all_codes):
        print('C' if cycles_all_codes[i] else 'P', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))
        if args.f:
            print('C' if cycles_all_codes[i] else 'P', end=' ')
            print(' '.join([bin(c)[2::].zfill(n) for c in code]))
        
        if args.m:
            bin_words = [bin(c)[2::].zfill(n) for c in code]
            for i in range(n):
                print(' '.join([b[::-1][i] for b in bin_words]))

if args.c:
    for i, code in enumerate(all_codes):
        if not cycles_all_codes[i]:
            continue

        print('C', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))
        if args.f:
            print('C', end=' ')
            print(' '.join([bin(c)[2::].zfill(n) for c in code]))
        
        if args.m:
            bin_words = [bin(c)[2::].zfill(n) for c in code]
            for i in range(n):
                print(' '.join([b[::-1][i] for b in bin_words]))

if args.p:
    for i, code in enumerate(all_codes):
        if cycles_all_codes[i]:
            continue
        
        print('P', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))
        if args.f:
            print('P', end=' ')
            print(' '.join([bin(c)[2::].zfill(n) for c in code]))
        
        if args.m:
            bin_words = [bin(c)[2::].zfill(n) for c in code]
            for i in range(n):
                print(' '.join([b[::-1][i] for b in bin_words]))

if args.b:
    for i, code in enumerate(beckett_gray_codes):
        if not cycles_beckett_gray_codes[i]:
            continue
        
        print('B', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))
        if args.f:
            print('B', end=' ')
            print(' '.join([bin(c)[2::].zfill(n) for c in code]))
        
        if args.m:
            bin_words = [bin(c)[2::].zfill(n) for c in code]
            for i in range(n):
                print(' '.join([b[::-1][i] for b in bin_words]))

if args.u:
    for i, code in enumerate(beckett_gray_codes):
        if cycles_beckett_gray_codes[i]:
            continue
        
        print('U', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))
        if args.f:
            print('U', end=' ')
            print(' '.join([bin(c)[2::].zfill(n) for c in code]))
        
        if args.m:
            bin_words = [bin(c)[2::].zfill(n) for c in code]
            for i in range(n):
                print(' '.join([b[::-1][i] for b in bin_words]))

if args.r:
    codes = []
    if all_codes:
        if args.a:
            codes = all_codes.copy()
        elif args.c:
            codes = [code for  i, code in enumerate(all_codes.copy()) if cycles_all_codes[i]]
        else:
            codes = [code for  i, code in enumerate(all_codes.copy()) if not cycles_all_codes[i]]

    elif beckett_gray_codes:
        if args.b:
            codes = [code for  i, code in enumerate(beckett_gray_codes.copy()) if cycles_beckett_gray_codes[i]]
        else:
            codes = [code for  i, code in enumerate(beckett_gray_codes.copy()) if not cycles_beckett_gray_codes[i]]
    
    delta_sequences = build_delta_sequences(codes)
    isomorphisms = find_isomorphisms(delta_sequences, n)

    for seq in isomorphisms:
        pairs = list(isomorphisms[seq])
        for p in pairs:
            if seq < p:
                print(''.join([str(el) for el in get_delta_sequence(codes[seq])]) + " <=> " + ''.join([str(el) for el in get_delta_sequence(codes[p])]))

# Simple case with no args (default)
# simple case 


if args.a == False and args.b==False and  args.u==False and  args.c==False and  args.p==False and  args.r==False and  args.f==False and args.m==False:
    
    gc = [0]  # stack
    visited = [False] * 2**n
    visited[0] = True
    GC_DFS(1, gc[0], 0, n, gc, visited, all_codes, cycles_all_codes)
    for i, code in enumerate(all_codes):
        print('C' if cycles_all_codes[i] else 'P', end=' ')
        print(''.join([str(el) for el in get_delta_sequence(code)]))