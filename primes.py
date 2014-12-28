import sys

def primes(num):
    while(num):
        is_prime = True
        for i in range((num-1),1,-1):
            if num%i == 0 or num%2 == 0:
                is_prime = False
                break
        if(is_prime):
            print "%s is totally prime!" % num
        # else:
            # print "%s is not prime!" % num
        num-=1
        
def main(args):
    primes(int(args.pop()))
    
if __name__ == '__main__':
    main(sys.argv)