import re
from rdflib.term import Literal

class StatementComparator:
    def __init__(self, hashstr=None):
        self.hashstr = hashstr
    def compare(self, q1, q2):
        c = self.compare_context(q1, q2);
        if not c == 0: return c
        c = self.compare_subject(q1, q2);
        if not c == 0: return c
        c = self.compare_predicate(q1, q2);
        if not c == 0: return c
        return self.compare_object(q1, q2);
    def compare_context(self, q1, q2):
        r1 = q1[0]
        r2 = q2[0]
        if (r1 is None) and (r2 is None): return 0
        if (r1 is None) and (not r2 is None): return -1
        if (not r1 is None) and (r2 is None): return 1
        return self.compare_uri(str(r1), str(r2))
    def compare_subject(self, q1, q2):
        return self.compare_uri(str(q1[1]), str(q2[1]))
    def compare_predicate(self, q1, q2):
        return self.compare_uri(str(q1[2]), str(q2[2]))
    def compare_object(self, q1, q2):
        r1 = q1[3]
        r2 = q2[3]
        if isinstance(r1, Literal) and not isinstance(r2, Literal): return 1
        if not isinstance(r1, Literal) and isinstance(r2, Literal): return -1
        if isinstance(r1, Literal):
            return self.compare_literal(r1, r2)
        else:
            return self.compare_uri(str(r1), str(r2))
    def compare_literal(self, l1, l2):
        x1 = str(l1)
        x2 = str(l2)
        if (x1 < x2): return -1
        if (x1 > x2): return 1
        x1 = l1.datatype
        x2 = l2.datatype
        if (x1 is None) and (not x2 is None): return -1
        if (not x1 is None) and (x2 is None): return 1
        if (not x1 is None) and (x1 < x2): return -1
        if (not x1 is None) and (x1 > x2): return 1
        x1 = l1.language
        x2 = l2.language
        if (x1 is None) and (not x2 is None): return -1
        if (not x1 is None) and (x2 is None): return 1
        if (not x1 is None) and (x1 < x2): return -1
        if (not x1 is None) and (x1 > x2): return 1
        return 0
    def compare_uri(self, s1, s2):
        p1 = s1
        p2 = s2
        if not self.hashstr is None:
            p1 = re.sub(self.hashstr, ' ', s1)
            p2 = re.sub(self.hashstr, ' ', s2)
        if p1 < p2: return -1
        if p1 == p2: return 0
        return 1
