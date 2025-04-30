class TestBase:
    def __init__(self,case1: [],case2: []):
        self.case1 = case1
        self.case2 = case2

    def run_test(self,solution,case_print):
        res = []
        for i in range(len(self.case1)):
            r = solution(self.case1[i])
            print(f'expect: {case_print(self.case1[i])}, res: {case_print(self.case2[i])}')
            res.append(r)
        print(res)