from xml.dom.expatbuilder import InternalSubsetExtractor


a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89])
b = set([1, 2, 3, 4, 5])
c = []

c = list(set(a.intersection(b)))
print(c)

