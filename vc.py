from typing import Callable
def main(op:Callable[[str],int],sentence:str):
    return op(sentence)

def vowel_count(sentence:str)->int:
    return len([char for char in sentence if char in 'aeiou'])

def cons_count(sentence:str)->int:
    return len([char for char in sentence if char in 'bcdfghjklmnpqrstvwxyz'])

if __name__ == '__main__':
    print(main(vowel_count,'I am going for the dinner would you like to join to the party mr. Punit'))
    print(main(cons_count,'I am going for the dinner would you like to join to the party mr. Punit'))

