from typing import List, Callable

# Helper Funcs
def power_set(nums: List[int]) -> List[List[int]]:
    """
    Get power set of a list of numbers
    """

    out = []
    def helper(i, curr):

        if i >= len(nums):
            out.append(curr[:])
            return
        
        helper(i+1, curr + [nums[i]])
        helper(i+1, curr) 
 
    helper(0, [])
    return out


def get_inverse(f: Callable, pre_image: List, domain: List) -> List:
    """
    Return f^(-1)(I).
    """ 
    output = []

    for domain_val in domain:
        if f(domain_val) in pre_image:
            output.append(domain_val)
            
    return output


def check_continuity(
        f: Callable,
        domain: List[int],
        tau_domain: List[List],
        tau_pre_image: List[List]
        ):
    """
    Return wether f is continuous
    For f to be contiuous all inverse sets of tauI must be in tauD.
    """
    tau_domain = set(tuple(sorted(x)) for x in tau_domain)

    for set_pre_image in tau_pre_image:
        if not tuple(get_inverse(f, set_pre_image, domain)) in tau_domain:
            return False
        
    return True