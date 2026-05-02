class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
            
        self.store[key].append((timestamp, value))

        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        values = self.store[key]

        left = 0
        right = len(values) - 1
        answer = ""
        while left <= right:
            m = (left + right) // 2

            current_timestamp, current_value = values[m]

            if current_timestamp <= timestamp:
                answer = current_value
                left = m + 1
            else:
                right = m - 1
        return answer
        
