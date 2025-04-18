# Count and Say – LeetCode Problem #38

A clean and optimized solution for the classic **Count and Say** problem on LeetCode, implemented in Python.

---

## 📌 Problem Statement

The **count-and-say** sequence is a series of digit strings defined recursively:

- **countAndSay(1)** = `"1"`
- **countAndSay(n)** is the run-length encoding of `countAndSay(n - 1)`

The sequence describes each previous term in terms of the count and value of its digits.

---

### 🧠 Example

### Input:
  n = 4 
### Output: 
  "1211"

**Explanation:**
- `countAndSay(1)` → `"1"`
- `countAndSay(2)` → `"11"` (one 1)
- `countAndSay(3)` → `"21"` (two 1s)
- `countAndSay(4)` → `"1211"` (one 2, one 1)

---

## ✅ Solution

```
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"  # Base case for n = 1

        for _ in range(n - 1):  # Loop n-1 times
            temp = ""
            i = 0
            while i < len(result):
                count = 1
                while i + 1 < len(result) and result[i] == result[i + 1]:
                    i += 1
                    count += 1
                temp += str(count) + result[i]
                i += 1
            result = temp

        return result
```
## 🛠️ How to Run
sol = Solution()
print(sol.countAndSay(4))  # Output: "1211"

# 🚀 About Coding Moves
**Coding Moves** is not just a name — it's a mission, a brand, and a future tech organization built with purpose and passion.
It represents the dream of empowering coders, solving real-world problems, and building next-gen software — starting with problems like this one.

💡 Powered by passion. Guided by purpose. Built with faith.
— <a href="https://www.youtube.com/@Coding_Moves">Coding Moves</a>

# 🤝 Connect
Stay tuned for more coding solutions, innovative projects, and future products under the Coding Moves banner, in shaa Allah.

  
