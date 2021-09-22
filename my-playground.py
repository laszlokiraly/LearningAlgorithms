import random

def tournament_allows_odd(A):
  is_odd = len(A) % 2 == 1
  if is_odd:
      A.append(-1)

  N = len(A)
  winner = [None] * (N-1)
  loser = [None] * (N-1)
  prior = [-1] * (N-1)             

  idx = 0
  for i in range(0, N, 2):         
    if A[i] < A[i+1]:
      winner[idx] = A[i+1]
      loser[idx] = A[i]
    else:
      winner[idx] = A[i]
      loser[idx] = A[i+1]
    idx += 1

  m = 0                            
  while idx < N-1:
    if winner[m] < winner[m+1]:    
      winner[idx] = winner[m+1]
      loser[idx]  = winner[m]
      prior[idx]  = m+1
    else:
      winner[idx] = winner[m]
      loser[idx]  = winner[m+1]
      prior[idx]  = m
    m += 2                         
    idx += 1

  largest = winner[m]
  second = loser[m]                
  m = prior[m]
  while m >= 0:
    if second < loser[m]:          
      second = loser[m]
    m = prior[m]

  return (largest, second)


def test_tournament_allows_odd():
    A = [3, 87 , 2]
    print((87, 3), tournament_allows_odd(A))

    # sanity check, doesn't prove anything....
    for _ in range(200):
        A = list(range(11))
        random.shuffle(A)
        if ((10, 9) != tournament_allows_odd(A)):
            print('oh no')

def counting_sort(A, M):
  counts = [0] * M
  for v in A:
    counts[v] += 1

  pos = 0
  v = 0
  while pos < len(A):
    for idx in range(counts[v]):
      A[pos+idx] = v
    pos += counts[v]
    v += 1

def counting_sort_improved(A, M):
  counts = [0] * M
  for v in A:
    counts[v] += 1

  pos = 0
  v = 0
  while pos < len(A):
    current_count = counts[v]
    if current_count > 0:
        A[pos:(pos+current_count)] = [v] * current_count
        pos += current_count
    v += 1

def test_counting_sort():
    original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    improved = original.copy()
    expected = sorted(original)
    counting_sort(original, 10)
    counting_sort_improved(improved, 10)

    print(expected)
    print(original)
    print(improved)

test_counting_sort()
test_tournament_allows_odd()
