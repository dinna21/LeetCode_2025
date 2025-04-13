
def generate_parenthesis(n):
    def backTrack(s,open_count,close_count):
        if len(s) == 2*n:
            result.append(s)
            return
        if open_count < n:
            backTrack(s+'(',open_count+1,close_count)
        if close_count < open_count:
            backTrack(s+')',open_count,close_count+1)
    result = []
    backTrack('',0,0)
    return result
print(generate_parenthesis(3))

