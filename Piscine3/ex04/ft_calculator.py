class calculator:
    
    @staticmethod
    def dotproduct(vec1, vec2):
        if len(vec1) != len(vec2):
            print("Vectors must be of the same length")
            return
        result = sum(x * y for x, y in zip(vec1, vec2))
        print(result)
        return result

    @staticmethod
    def add_vec(vec1, vec2):
        if len(vec1) != len(vec2):
            print("Vectors must be of the same length")
            return
        result = [float(x + y) for x, y in zip(vec1, vec2)]
        print(result)
        return result

    @staticmethod
    def sous_vec(vec1, vec2):
        if len(vec1) != len(vec2):
            print("Vectors must be of the same length")
            return
        result = [float(x - y) for x, y in zip(vec1, vec2)]
        print(result)
        return result

a = [5, 10, 2]
b = [2, 4, 3]
calculator.dotproduct(a,b)
calculator.add_vec(a,b)
calculator.sous_vec(a,b)