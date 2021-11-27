
"""
Combine two linguistic terms.

a and b are functions of two sets of the same domain.

Since these combinators are used directly in the Set class to implement logic operations, 
the most obvious use of this module is when subclassing Set to make use of specific combinators
for special circumstances.

Most functions also SHOULD support an arbitrary  number of arguments so they can be used in
other contexts than just fuzzy sets. HOWEVER, mind that the primary set of arguments always are functors and
there is always only one secondary argument - the value to be evaluated.
"""

from functools import reduce

from numpy import multiply

from .functions import noop


def MIN(*funcs):
    """Classic AND variant."""
    def F_MIN(z):
        return min(f(z) for f in funcs)
    return F_MIN


def MAX(*funcs):
    """Classic OR variant."""
    def F_MAX(z):
        return max(f(z) for f in funcs)
    return F_MAX


def product(*funcs):
    """AND variant."""
    def F_product(z):
        return reduce(multiply, (f(z) for f in funcs))
    return F_product


def bounded_sum(a, b):
    """OR variant."""
    # TODO: Expand..
    def f_bounded_sum(z):
        x, y = a(z), b(z)
        return x + y - x * y
    return f_bounded_sum

def lukasiewicz_AND(a, b):
    """AND variant."""
    # TODO: Expand..
    def f_lukasiewicz_AND(z):
        x, y = a(z), b(z)
        return min(1, x + y)
    return f_lukasiewicz_AND

def lukasiewicz_OR(a, b):
    """OR variant."""
    # TODO: Expand..
    def f_lukasiewicz_OR(z):
        x, y = a(z), b(z)
        return max(0, x + y - 1)
    return f_lukasiewicz_OR

def einstein_product(a, b):
    """AND variant."""
    # TODO: Expand..
    def f_einstein_product(z):
        x, y = a(z), b(z)
        return (x * y) / (2 - (x + y - x * y))
    return f_einstein_product

def einstein_sum(a, b):
    """OR variant."""
    # TODO: Expand..
    def f_einstein_sum(z):
        x, y = a(z), b(z)
        return (x + y) / (1 + x * y)
    return f_einstein_sum

def hamacher_product(a, b):
    """AND variant.
    
    (xy) / (x + y - xy) for x, y != 0
    0 otherwise
    """
    # TODO: Expand..
    def f_hamacher_product(z):
        x, y = a(z), b(z)
        return (x * y) / (x + y - x * y) if x != 0 and y != 0 else 0
    return f_hamacher_product

def hamacher_sum(a, b):
    """OR variant.
    
    (x + y - 2xy) / (1 - xy) for x,y != 1
    1 otherwise
    """
    # TODO: Expand..
    def f_hamacher_sum(z):
        x, y = a(z), b(z)
        return (x + y - 2 * x * y) / (1 - x * y) if x != 1 or y != 1 else 1
    return f_hamacher_sum


def lambda_op(l):
    """A 'compensatoric' operator, combining AND with OR by a weighing factor l.
    
    This complicates matters a little, since all combinators promise to just take 
    2 functions as arguments, so we parametrize this with l.
    """
    # TODO: Expand..
    assert (0 <= l <= 1)
        
    def e(a, b):
        def f_lambda_op(z):
            x, y = a(z), b(z)
            return l * (x * y) + (1 - l) * (x + y - x * y)
        return f
    return e


def gamma_op(g):
    """Combine AND with OR by a weighing factor g.
    
    This is called a 'compensatoric' operator.
    
    g (gamma-factor)
        0 < g < 1 (g == 0 -> AND; g == 1 -> OR)
        
    Same problem as with lambda_op, since all combinators promise to just take 
    2 functions as arguments, so we parametrize this with g.
    """
    # TODO: Expand..
    assert (0 <= g <= 1)
    
    def e_gamma_op(a, b):
        def f_gamma_op(z):
            x, y = a(z), b(z)
            return (x * y) ** (1 - g) * ((1 - x) * (1 - y)) ** g
        return f_gamma_op
    return e_gamma_op

def simple_disjoint_sum(*funcs):
    """Simple fuzzy XOR operation.
    Someone fancy a math proof?
    
    Basic idea:
    (A AND ~B) OR (~A AND B)
    
    >>> xor = simple_disjoint_sum(noop(), noop())
    >>> xor(0)
    0
    >>> xor(1)
    0
    >>> xor(0.5)
    0.5
    >>> xor(0.3) == round(xor(0.7), 2)
    True
    
    Attempt for expansion without proof:
    x = 0.5
    y = 1
    (x and ~y) or (~x and b)

    max(min(0.5, 0), min(0.5, 1)) == 0.5

    ----

    x = 0
    y = 0.5
    z = 1

    (A AND ~B AND ~C) OR (B AND ~A AND ~C) OR (C AND ~B AND ~A)
    max(min(0,0.5,0), min(0.5,1,0), min(1,0.5,1)) == 0.5
    """
    def F_simple_disjoint_sum(z):
        # Reminder how it works for 2 args
        #x, y = a(z), b(z)  
        #return max(min(x, 1-y), min(1-x, y))  
        
        M = {f(z) for f in funcs}  # a set of all membership values over all given functions to be iterated over
        # we need to go over each value in the set, calc min(x, inverse(rest)), from that calc max
        # for x in args:
        # print(x, [1-y for y in args-set([x])])
        
        # FYI: this works because M-set([x]) returns a new set without x, which we use to construct a new set
        # with inverted values - however, if M only has one value, which is the case if all given values are equal -
        # we have to handle an empty generator expression, which the "or (1-x,)" does.
        # Lastly, the *(...) is needed because min only takes one single iterator, so we need to unzip the rest.
        return max(min((x, *({1-y for y in M-set([x])} or (1-x,)) ))
                   for x in M)
    return F_simple_disjoint_sum
