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


def get_inverse(f: Callable, image: List, domain: List) -> List:
    """
    Return f^(-1)(I).
    """ 
    pre_image = []

    for x in domain:
        y = f(x)
        if y in image:
            pre_image.append(x)

            
    return pre_image


def check_continuity(
        f: Callable,
        tau_domain: List[List],
        tau_image: List[List]
        ):
    """
    Return whether f is continuous
    For f to be contiuous all sets from tau_image must be removed
    Sets are removed if a set from the domain after going through f is in tau_image.
    """

    tau_image = set(tuple(sorted(x)) for x in tau_image)

    for set_from_domain in tau_domain:
        y_set_from_domain = set([f(x) for x in set_from_domain])
        y_set_from_domain = tuple(sorted(y_set_from_domain))

        if y_set_from_domain in tau_image:
            tau_image.remove(y_set_from_domain)

    return len(tau_image) == 0