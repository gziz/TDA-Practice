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
    inverse_vals = []

    for domain_val in domain:
        if f(domain_val) in pre_image:
            inverse_vals.append(domain_val)
            
    return inverse_vals


def check_continuity(
        f: Callable,
        domain: List[int],
        tau_domain: List[List],
        tau_pre_image: List[List]
        ):
    """
    Return whether f is continuous
    For f to be contiuous all inverse sets of tau_pre_image must be part of tau_domain.
    """
    # Sort tau sets to avoid false positives when 
    # comparing sets with same elements but different order
    tau_domain = set(tuple(sorted(x)) for x in tau_domain)

    for set_pre_image in tau_pre_image:
        if not tuple(get_inverse(f, set_pre_image, domain)) in tau_domain:
            return False
        
    return True