#################################################################>>> 팰린드롬
#Input: "A man, a plan, a canal: Panama"
#Output: true
#############################################################333333333333333

def isPalindrome(self, s: str) -> bool:
    strs = []
    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    print(strs)

    while len(strs) > 1:
        if strs.pop(0) != strs.pop():
            return False

    return True

#pop()은 리스트에서 맨 마지막 요소를 출력하면서 그 요소를 리스트에서 삭제하는, 즉 리스트에서 꺼내버리는 함수.
#하나의 인자를 넣어주면 x위치에 있는 요소를 꺼내게 됨.

def isPalindrome(s):
    # 자료형 데크로 선언
    strs: Deque = collections.deque()

    for char in s:
        if char.isalnum():
            strs.append(char.lower())

    while len(strs)>1:
        if strs.popleft() != strs.pop():
            return False

    return True

isPalindrome("A man, a plan, a canal: Panama")


def isPalindrome(self, s:str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]','',s)

    return s == s[::-1] #슬라이d


####################################################################### 문자열 뒤집기
#Input: ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
######################################################################

def reverseString(self, s: List[str]) -> None:
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


def reverseString(self, s: List[str]) -> None:
    s.reverse()

###################################################################### 로그 파일 재정렬
#Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
#Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
########################################################################################

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digit = [][]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits


log = "dig1 8 1 5 1"
print(log.split()[1])

###################################################################### 가장 흔한 단어
#Input:
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
#Output: "ball"
########################################################################################
def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    #가장흔하게등장하는 단어의 첫번째 인덱스를 리턴
    return counts.most_common(1)[0][0]

mostCommonWord()

import re
import collections
paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
def mostCommonWord(paragraph, banned):
    words = [word for word in re.sub(r'[^\w]',' ',paragraph).lower().split() if word not in banned]
    counts = collections.Counter(words)
    #가장흔하게등장하는 단어의 첫번째 인덱스를 리턴
    return counts.most_common(1)[0][0]

mostCommonWord(paragraph,banned)

###################################################################### 가장 흔한 단어
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
########################################################################################
def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdic(list)

    for word in strs:
        anagrams[''.join(sorted(word))].append(word)
    return anagrams.values()
