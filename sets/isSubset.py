def isSubset(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True

nums1 = {i for i in input("Enter set 1 elements separated by space: ").split()}
nums2 = {i for i in input("Enter set 2 elements separated by space: ").split()}

if isSubset(nums1, nums2):
    print("Set 1 is a subset of Set 2")
else:
    print("Set 1 is not a subset of Set 2")